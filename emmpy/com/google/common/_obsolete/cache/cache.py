"""emmpy.package com.google.common.cache.cache

N.B. This class was created from a Java interface, and therefore most of these
methods will raise exceptions if invoked.
"""


class Cache:
    """Cache

     Copyright (C) 2011 The Guava Authors

    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use this file except in compliance with the License. You may obtain a copy
    of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations
    under the License.
    """

    def __init__(self):
        """Constructor

        INTERFACE - DO NOT INSTANTIATE

        A semi-persistent mapping from keys to values. Cache entries are
        manually added using get(Object, Callable) or put(Object, Object), and
        are stored in the cache until either evicted or manually invalidated.
        The common way to build instances is using CacheBuilder.

        Implementations of this interface are expected to be thread-safe, and
        can be safely accessed by multiple concurrent threads.

        @author Charles Fry
        @since 10.0
        """
        raise Exception

    def getIfPresent(self, key):
        """Returns the value associated with key in this cache, or None if
        there is no cached value for key.

        INTERFACE - DO NOT INOKE

        @since 11.0
        """
        raise Exception

    def get(self, key, loader):
        """Returns the value associated with key in this cache, obtaining that
        value from loader if necessary.

        INTERFACE - DO NOT INVOKE

        The method improves upon the conventional "if cached, return; otherwise
        create, cache and return" pattern. For further improvements, use
        LoadingCache} and its get(Object) get(K) method instead of this one.

        Among the improvements that this method and LoadingCache.get(K) both
        provide are:

        LoadingCache.get(Object) awaiting the result of a pending load rather
        than starting a redundant one
        eliminating the error-prone caching boilerplate
        tracking load statistics

        Among the further improvements that LoadingCache can provide but this
        method cannot:

        consolidation of the loader logic to CacheBuilder.build(CacheLoader)
        a single authoritative location
        LoadingCache.refresh refreshing of entries}, including
        CacheBuilder.refreshAfterWrite automated refreshing
        LoadingCache.getAll bulk loading requests, including
        CacheLoader#loadAll bulk loading implementations

        Warning: For any given key, every loader used with it should compute
        the same value. Otherwise, a call that passes one loader may return
        the result of another call with a differently behaving loader For
        example, a call that requests a short timeout for an RPC may wait for
        a similar call that requests a long timeout, or a call by an
        unprivileged user may return a resource accessible only to a privileged
        user making a similar call. To prevent this problem, create a key
        object that includes all values that affect the result of the query.
        Or use LoadingCache.get(K), which lacks the ability to refer to state
        other than that in the key.

        Warning: as with  CacheLoader.load, loader must not return null; it may
        either return a non-null value or throw an exception.

        No observable state associated with this cache is modified until
        loading completes.

        @throws ExecutionException if a checked exception was thrown while
        loading the value
        @throws UncheckedExecutionException if an unchecked exception was
        thrown while loading the value
        @throws ExecutionError if an error was thrown while loading the value
        @since 11.0
        """
        raise Exception

    def getAllPresent(self, keys):
        """Returns a map of the values associated with {@code keys} in this
        cache.

        INTERFACE - DO NOT INVOKE

        The returned map will only contain entries which are already present in
        the cache.

        @since 11.0
        """
        raise Exception

    def put(self, key, value):
        """Associates {@code value} with {@code key} in this cache.

        INTERFACE - DO NOT INVOKE

        If the cache previously contained a value associated with key, the old
        value is replaced by value.

        Prefer get(Object, Callable) when using the conventional "if cached,
        return; otherwise create, cache and return" pattern.

        @since 11.0
        """
        raise Exception

    def putAll(self, m):
        """Copies all of the mappings from the specified map to the cache.

        INTERFACE - DO NOT INVOKE

        The effect of this call is equivalent to that of calling put(k, v) on
        this map once for each mapping from key k to value v in the specified
        map. The behavior of this operation is undefined if the specified map
        is modified while the operation is in progress.

        @since 12.0
        """
        raise Exception

    def invalidate(self, key):
        """Discards any cached value for key key.

        INTERFACE - DO NOT INVOKE
        """
        raise Exception

    def invalidateAll(self, *args):
        if len(args) == 0:
            # Discards all entries in the cache.
            raise Exception
        elif len(args) == 1:
            (keys,) = args
            # Discards any cached values for keys keys.
            # @since 11.0
            raise Exception
        else:
            raise Exception

    def size(self):
        """Returns the approximate number of entries in this cache.

        INTERFACE - DO NOT INVOKE
        """
        raise Exception

    def stats(self):
        """Returns a current snapshot of this cache's cumulative statistics, or
        a set of default values if the cache is not recording statistics.

        INTERFACE - DO NOT INVOKE

        All statistics begin at zero and never decrease over the lifetime of
        the cache.

        Warning: this cache may not be recording statistical data. For example,
        a cache created using CacheBuilder only does so if the
        CacheBuilder.recordStats method was called. If statistics are not being
        recorded, a CacheStats instance with zero for all values is returned.
        """
        raise Exception

    def asMap(self):
        """Returns a view of the entries stored in this cache as a thread-safe
        map.

        INTERFACE - DO NOT INVOKE

        Modifications made to the map directly affect the cache.

        Iterators from the returned map are at least weakly consistent: they
        are safe for concurrent use, but if the cache is modified (including by
        eviction) after the iterator is created, it is undefined which of the
        changes (if any) will be reflected in that iterator.
        """
        raise Exception

    def cleanUp(self):
        """Performs any pending maintenance operations needed by the cache.

        INTERFACE - DO NOT INVOKE

        Exactly which activities are performed -- if any -- is
        implementation-dependent.
        """
        raise Exception
