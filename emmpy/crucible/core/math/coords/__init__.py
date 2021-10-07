"""Python port of Java classes from the coords hierarchy.

From the original package-info.java:

This package provides the ability to easily convert between Cartesian and
several coordinate systems (such as spherical) and the associated states.

Key classes are:

CoordConverters
    The user should be able to get most of the desired functionality by
    using the CoordConverters class. This class contains static methods
    allowing for the conversion from Cartesian coordinates to the intended
    coordinate and vice versa. It also has the equivalent state
    conversion. If a user needs to convert between two coordinate systems,
    they are forced to go through Cartesian. If this becomes a performance
    burden for a user, the framework allows for direct coordinate
    conversion to be added.

    These static methods are intended to be thread safe, although they
    need system tests.

    When the user asks for a conversion, they will receive a concrete
    container class containing the information for that coordinate e.g. 
    SphericalCoord has three field for Radius, Colatitude, and Longitude.
    These classes mirror the VectorIJK and the StateVector classes and
    also follow the Writable pattern.

    The only public classes are the before mentioned container classes and
    the CoordConverters class.

    Precautions were taken to make CoordConverters thread safe.

For developers
    The work is done by implementations of the CoordConverter interface.
    This interface, along with its implementations are intended to be
    package private, although they may be useful in other contexts. The
    Jacobian interface, also a package private, is meant to assist the
    CoordConverter implementations by providing a way to manipulate the
    Jacobians.

    If a new type is added to the CoordConverters, six classes must be
    added. Two Coordinate classes, one unwritable and one unwritable. The
    unwritable should extend the abstract helper class Coordinate and the
    writable should extend the writable, and make public the setters
    inherited from the abstract class. Two State classes, one unwritable
    and one unwritable. The state classes follow the same pattern, the
    unwritable extends an abstract helper class State and the writable
    extends the unwritable. One CoordConverter implementation, and one
    Jacobian although this is not specifically required, it should help.
    And then the four methods should be added to CoordConverters.

Modules
-------
abstractcoordconverter.py
abstractcoordconverterij.py
abstractvectorfieldvalue.py
cartesianvectorfieldvalue.py
coordconverter.py
coordconverterij.py
coordconverters.py
cylindricalcoordconverter.py
cylindricaltocartesianbasistransformation.py
cylindricaltocartesianjacobian.py
cylindricalvectorfieldvalue.py
latitudinalcoordconverter.py
latitudinaltocartesianjacobian.py
pointonaxisexception.py
polarcoordconverter.py
polartocartesianjacobian.py
radeccoordconverter.py
sphericalcoordconverter.py
sphericaltocartesianbasistransformation.py
sphericaltocartesianjacobian.py
sphericalvectorfieldvalue.py
transformation.py
transformationij.py
vectorfieldvalue.py
vectorfieldvalueconversions.py

Packages
--------
tests
"""
