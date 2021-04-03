"""emmpy.crucible.core.exceptions

Python port of Java classes from the crucible.core.exceptions hierarchy.

From the original package-info.java:

This package contains the parent classes of exception classes created in
support of the crucible library. In general, exceptions contained within
the library should descend from either CrucibleException or
CrucibleRuntimeException.

This will allow developers utilizing the library the ability to trap
exceptions specific to crucible itself without much difficulty.

@crucible.reliability reliable
@crucible.volatility semistable
@crucible.disclosure group

@see crucible.core.exceptions.CrucibleException
@see crucible.core.exceptions.CrucibleRuntimeException

Modules
-------
bugexception.py
crucibleexception.py
crucibleruntimeexception.py
functionevaluationexception.py
runtimeinterruptedexception.py
"""
