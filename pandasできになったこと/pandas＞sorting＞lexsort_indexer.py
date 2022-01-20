    def sort_values(  # type: ignore[override]
        self,
        by,
        axis: Axis = 0,
        ascending=True,
        inplace: bool = False,
        kind: str = "quicksort",
        na_position: str = "last",
        ignore_index: bool = False,
        key: ValueKeyFunc = None,
    ):
        inplace = validate_bool_kwarg(inplace, "inplace")
        axis = self._get_axis_number(axis)

        if not isinstance(by, list):
            by = [by]
        if is_sequence(ascending) and len(by) != len(ascending):
            raise ValueError(
                f"Length of ascending ({len(ascending)}) != length of by ({len(by)})"
            )
        if len(by) > 1:

            keys = [self._get_label_or_level_values(x, axis=axis) for x in by]

            # need to rewrap columns in Series to apply key function
            if key is not None:
                # error: List comprehension has incompatible type List[Series];
                # expected List[ndarray]
                keys = [
                    Series(k, name=name)  # type: ignore[misc]
                    for (k, name) in zip(keys, by)
                ]

            indexer = lexsort_indexer(
                keys, orders=ascending, na_position=na_position, key=key
            )
        elif len(by):

            by = by[0]
            k = self._get_label_or_level_values(by, axis=axis)

            # need to rewrap column in Series to apply key function
            if key is not None:
                # error: Incompatible types in assignment (expression has type
                # "Series", variable has type "ndarray")
                k = Series(k, name=by)  # type: ignore[assignment]

            if isinstance(ascending, (tuple, list)):
                ascending = ascending[0]

            indexer = nargsort(
                k, kind=kind, ascending=ascending, na_position=na_position, key=key
            )
        else:
            return self.copy()

        new_data = self._mgr.take(
            indexer, axis=self._get_block_manager_axis(axis), verify=False
        )

        if ignore_index:
            new_data.set_axis(
                self._get_block_manager_axis(axis), ibase.default_index(len(indexer))
            )

        result = self._constructor(new_data)
        if inplace:
            return self._update_inplace(result)
        else:
            return result.__finalize__(self, method="sort_values")
        
        
        
        
        
        
        
        
        
# この関数のappendが間接的ではなく、直接入れているのが気になる。

def lexsort_indexer(
    keys, 
    orders=None, 
    na_position: str = "last", 
    keys = None
) -> np.ndarray:
    """
    Performs lexical sorting on a set of keys

    Parameters
    ----------
    keys : sequence of arrays
        Sequence of ndarrays to be sorted by the indexer
    orders : bool or list of booleans, optional
        Determines the sorting order for each element in keys. If a list,
        it must be the same length as keys. This determines whether the
        corresponding element in keys should be sorted in ascending
        (True) or descending (False) order. if bool, applied to all
        elements as above. if None, defaults to True.
    na_position : {'first', 'last'}, default 'last'
        Determines placement of NA elements in the sorted list ("last" or "first")
    key : Callable, optional
        Callable key function applied to every element in keys before sorting

        .. versionadded:: 1.0.0

    Returns
    -------
    np.ndarray[np.intp]
    """
    from pandas.core.arrays import Categorical

    labels = []
    shape = []
    if isinstance(orders, bool):
        orders = [orders] * len(keys)
    elif orders is None:
        orders = [True] * len(keys)

    keys = [ensure_key_mapped(k, key) for k in keys]

    for k, order in zip(keys, orders):
        cat = Categorical(k, ordered=True)

        if na_position not in ["last", "first"]:
            raise ValueError(f"invalid na_position: {na_position}")

        n = len(cat.categories)
        codes = cat.codes.copy()

        mask = cat.codes == -1
        if order:  # ascending
            if na_position == "last":
                codes = np.where(mask, n, codes)
            elif na_position == "first":
                codes += 1
        else:  # not order means descending
            if na_position == "last":
                codes = np.where(mask, n, n - codes - 1)
            elif na_position == "first":
                codes = np.where(mask, 0, n - codes)
        if mask.any():
            n += 1

        shape.append(n)
        labels.append(codes)

    return indexer_from_factorized(labels, tuple(shape))