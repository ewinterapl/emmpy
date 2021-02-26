"""emmpy.crucible.core.collections

Python port of Java classes from the crucible.core.collections hierarchy.

From the original package-info.java:

Package containing Java collections framework related software.

This package simply contains any additional capabilities that are supplied and
designed to integrate with or into the general collections framework provided
by Sun.

Features include the following:

* Indexed based searching, namely utilities like locate the element last less
than or equal to an element in an existing list.
* Flattening iterators, that turn various combinations of iterators and
iterables of iterators and iterables into a single flat iterator.
* Filtering iterators, that take an iterator and a filter and produce an
iterator that only presents elements that pass the filter.

@crucible.reliability reliable
@crucible.volatility semistable
@crucible.disclosure group

package crucible.core.collections;

Modules
-------
abstractindexediterator.py
abstractreadonlylist.py
abstractsequentialreadonlylist.py
arrayutilities.py
basicreference.py
collectionutilities.py
indexrange.py
reference.py

Packages
--------
tests
"""
