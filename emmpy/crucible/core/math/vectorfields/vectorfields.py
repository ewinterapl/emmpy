"""emmpy.crucible.core.math.vectorfields.vectorfields

Author : vandejd1 Created : Feb 27, 2012

Copyright (C) 2012 The Johns Hopkins University Applied Physics Laboratory
(JHU/APL) All rights reserved
"""


# package crucible.core.math.vectorfields;
# import com.google.common.base.Predicate;
# import com.google.common.cache.Cache;
# import com.google.common.cache.CacheBuilder;
# import crucible.core.math.functions.DifferentiableUnivariateFunction;
# import crucible.core.math.functions.DifferentiableVectorIJKFunction;
# import crucible.core.math.functions.UnivariateFunction;
# import crucible.core.math.functions.VectorIJKFunction;
# import crucible.core.math.vectorfields.DifferentiableVectorField.Results;
# import crucible.core.math.vectorspace.UnwritableRotationMatrixIJK;
# import crucible.core.math.vectorspace.UnwritableVectorIJK;
# import crucible.core.math.vectorspace.VectorIJK;

from emmpy.crucible.core.math.vectorfields.vectorfield import VectorField


class VectorFields:
    """static convenience methods for creating vector fields

    Not all returned implementations are thread safe

    author vandejd1
    author G.K.Stephens
    """

    def __init__(self):
        """Constructor

        DO NOT INSTANTIATE
        """
        raise Exception

    #   /**
    #    * Creates a {@link VectorField} where the returned value is the same value as the supplied input.
    #    * 
    #    * @return a newly constructed {@link VectorField} where the returned value is the same as the
    #    *         supplied input
    #    */
    #   public static VectorField createIdentity() {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         return buffer.setTo(location);
    #       }
    #     };
    #   }

    #   /**
    #    * convert a univariate vector field (sampled at a given value of the independent variable) to a
    #    * vector field
    #    * 
    #    * @param field
    #    * @param x
    #    * @return
    #    */
    #   public static VectorField createSampled(final UnivariateVectorField field, final double x) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         return field.evaluate(x, location, buffer);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field that always returns the supplied vector
    #    * 
    #    * @return a newly created vector field
    #    */
    #   public static VectorField constantField(final UnwritableVectorIJK vector) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(@SuppressWarnings("unused") UnwritableVectorIJK location,
    #           VectorIJK buffer) {
    #         return buffer.setTo(vector);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by adding the two supplied vector fields.
    #    * 
    #    * @param a a vector field
    #    * @param b another vector field
    #    * @return a newly created vector field that computes the component-wise sum
    #    *         <code>( a + b )</code>
    #    */
    #   public static VectorField add(final VectorField a, final VectorField b) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         UnwritableVectorIJK aVect = a.evaluate(location);
    #         UnwritableVectorIJK bVect = b.evaluate(location);
    #         return VectorIJK.add(aVect, bVect, buffer);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by adding all the supplied vector fields.
    #    * 
    #    * @param fields a varargs of vector fields
    #    * @return a newly created vector field that computes the component-wise sum
    #    *         <code>( a + b + ...)</code> of all the vector fields
    #    */
    #   public static VectorField addAll(final VectorField... fields) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         double fx = 0.0;
    #         double fy = 0.0;
    #         double fz = 0.0;
    #         for (VectorField field : fields) {
    #           field.evaluate(location, buffer);
    #           fx += buffer.getI();
    #           fy += buffer.getJ();
    #           fz += buffer.getK();
    #         }
    #         return buffer.setTo(fx, fy, fz);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by negating the output of the supplied vector field. The location is not
    #    * negated.
    #    * 
    #    * @param field a vector field
    #    * @return a newly created vector field that negates the value of the input field
    #    */
    #   public static VectorField negate(final VectorField field) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         return field.evaluate(location, buffer).negate();
    #       }
    #     };
    #   }

    @staticmethod
    def scale(field, scaleFactor):
        """Creates a vector field by scaling the output of the supplied vector
        field.

        The location is not scaled.

        param field a vector field
        param scaleFactor a value to scale the output
        return a newly created vector field that computes the scale
        ( a*scaleFactor )
        """
        vf = VectorField()
        vf.evaluate = (
            lambda my_self, location, buffer:
            field.evaluate(location, buffer).scale(scaleFactor)
        )
        return vf

    #   /**
    #    * Creates a vector field by scaling the input location vector of the supplied vector field.
    #    * 
    #    * @param field a vector field
    #    * @param scaleFactor a value to scale the location vector
    #    * @return a newly created vector field that scales the input location vector
    #    *         <code>( location*scaleFactor  )</code>
    #    */
    #   public static VectorField scaleLocation(final VectorField field, final double scaleFactor) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         return field.evaluate(new UnwritableVectorIJK(scaleFactor, location), buffer);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by multiplying the supplied scalar field with the supplied vector field.
    #    * 
    #    * @param a a scalar field
    #    * @param b a vector field
    #    * @return a newly created vector field that computes the multiplication
    #    *         <code>( a<b> b </b> )</code>
    #    */
    #   public static VectorField multiply(final ScalarField a, final VectorField b) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         b.evaluate(location, buffer);
    #         return buffer.scale(a.evaluate(location));
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by multiplying the supplied scalar field with the supplied vector field.
    #    * 
    #    * @param a a vector field
    #    * @param b another vector field
    #    * @return a newly created vector field that computes the multiplication
    #    *         <code>( <b>a</b> x <b>b</b> )</code>
    #    */
    #   public static VectorField cross(final VectorField a, final VectorField b) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         UnwritableVectorIJK aVect = a.evaluate(location);
    #         b.evaluate(location, buffer);
    #         return VectorIJK.cross(aVect, buffer, buffer);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by from the supplied component scalar fields.
    #    * 
    #    * @param iField a scalar field
    #    * @param jField a scalar field
    #    * @param kField a scalar field
    #    * @return a newly created vector field that is a view of the three supplied component scalar
    #    *         fields
    #    */
    #   public static VectorField compose(final ScalarField iField, final ScalarField jField,
    #       final ScalarField kField) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         return buffer.setTo(iField.evaluate(location), jField.evaluate(location),
    #             kField.evaluate(location));
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a unitized vector field by from the supplied vector scalar field, an exception is
    #    * thrown if the supplied field contains the zero vector.
    #    * 
    #    * @param field a vector field
    #    * @return a newly created vector field that is a view of the supplied field where the vector has
    #    *         been unitized
    #    */
    #   public static VectorField unitize(final VectorField field) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         field.evaluate(location, buffer);
    #         return buffer.unitize();
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a unitized vector field by from the supplied vector scalar field, if the field has a
    #    * value of the zero vector, the zero vector is returned, unlike the {@link #unitize(VectorField)}
    #    * method which throws an exception instead.
    #    * 
    #    * @param field a vector field
    #    * @return a newly created vector field that is a view of the supplied field where the vector has
    #    *         been unitized
    #    */
    #   public static VectorField unitizeZero(final VectorField field) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         field.evaluate(location, buffer);
    #         if (buffer.getI() == 0.0 && buffer.getJ() == 0.0 && buffer.getK() == 0.0) {
    #           return buffer;
    #         }
    #         return buffer.unitize();
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a new vector field that is a rotated view of the supplied field.
    #    * <p>
    #    * If the supplied field is in reference frame A, and the supplied rotation matrix is supplied
    #    * that rotates FROM frame B TO reference frame A, then this will return a field in reference
    #    * frame B.
    #    * 
    #    * @param field a vector field in reference frame A
    #    * @param UnwritableRotationMatrixIJK a matrix that rotates from reference frame B to A
    #    * @return a newly created vector field in reference frame B
    #    */
    #   public static VectorField rotate(final VectorField field,
    #       final UnwritableRotationMatrixIJK matrix) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         // rotate the location
    #         VectorIJK rotated = matrix.mxv(location);
    #         // evaluate using the rotated vector
    #         field.evaluate(rotated, buffer);
    #         // rotate the field value back
    #         return matrix.mtxv(buffer, buffer);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field by offsetting the input location vector of the supplied vector.
    #    * 
    #    * @param field a vector field
    #    * @param offset a vector to offset the location vector
    #    * @return a newly created vector field that offsets the input location vector by another vector
    #    *         <code>( location + offset  )</code>
    #    */
    #   public static VectorField offset(final VectorField field, final UnwritableVectorIJK offset) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         return field.evaluate(VectorIJK.add(location, offset), buffer);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a new vector field by filtering the supplied vector field using the supplied
    #    * {@link Predicate}. If true, the value of the supplied field is returned, if false, the supplied
    #    * fill value is returned.
    #    * 
    #    * @param field a vector field to be filtered
    #    * @param retainIfTrue a Predicate to be used as a filter when false is returned
    #    * @param fillValue the value to return if the filter returns false
    #    * @return a newly created vector field that is a filtered view of the supplied field
    #    */
    #   public static VectorField filter(final VectorField field,
    #       final Predicate<UnwritableVectorIJK> retainIfTrue, UnwritableVectorIJK fillValue) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         boolean retain = retainIfTrue.apply(location);
    #         if (retain) {
    #           return field.evaluate(location, buffer);
    #         }
    #         return buffer.setTo(fillValue);
    #       }
    #     };
    #   }

    #   /**
    #    * If evaluating the Vector field is expensive, and you want to lazily evaluate and save the
    #    * values for future retrieval, then this method provides a wrapper implementation that caches the
    #    * values of the {@link VectorField}. Set the maxItemsToCache to the most you want to cache.
    #    * <p>
    #    * NOTE: this is not view safe, if the input {@link VectorField} is changing, this will not be
    #    * reflected in the returned {@link VectorField}.
    #    * 
    #    * @param expensiveToComputeField
    #    * @param maxItemsToCache
    #    * @return a newly created vector field that lazily caches the values of the field at a given
    #    *         location
    #    */
    #   public static VectorField withCache(final VectorField expensiveToComputeField,
    #       int maxItemsToCache) {
    #     final Cache<UnwritableVectorIJK, UnwritableVectorIJK> cache =
    #         CacheBuilder.newBuilder().maximumSize(maxItemsToCache).build();
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         // make a defensive copy!
    #         // TODO this may unnecessarily be making a copy, you could make
    #         // the copy only on insertion, but this is a bit more thread
    #         // safe
    #         UnwritableVectorIJK locationCopy = UnwritableVectorIJK.copyOf(location);
    #         UnwritableVectorIJK vector = cache.getIfPresent(locationCopy);
    #         if (vector == null) {
    #           UnwritableVectorIJK obj = expensiveToComputeField.evaluate(locationCopy);
    #           cache.put(locationCopy, obj);
    #           return buffer.setTo(obj);
    #         } else {
    #           return buffer.setTo(vector);
    #         }
    #       }
    #     };
    #   }

    #   /**
    #    * Performs the following Composition:
    #    * <p>
    #    * <b>OutputVectorFuction</b>(t) = <b>Field</b>(<b>Path</b>(t))
    #    * 
    #    * @param field a {@link VectorField}
    #    * @param path a path through the field parameterized on t
    #    * @return a newly constructed {@link VectorIJKFunction}
    #    */
    #   public static VectorIJKFunction compose(final VectorField field, final VectorIJKFunction path) {
    #     return new VectorIJKFunction() {
    #       @Override
    #       public VectorIJK evaluate(double t, VectorIJK buffer) {
    #         return buffer.setTo(field.evaluate(path.evaluate(t, buffer), buffer));
    #       }
    #     };
    #   }

    #   /**
    #    * Computes the integrand for line integrals of {@link VectorField}s.
    #    * <p>
    #    * <b>F</b>(<b>r</b>)&#8901;d<b>r</b> = <b>G</b>(t) = <b>F</b>(<b>r</b>(t))&#8901;<b>r</b>'(t)*dt
    #    * <p>
    #    * See http://en.wikipedia.org/wiki/Line_integral# Line_integral_of_a_vector_field
    #    * 
    #    * @param field a {@link VectorField}
    #    * @param path a {@link DifferentiableUnivariateFunction} defining a path through the field
    #    *        parameterized on t, for which the derivative as a function of t is known
    #    * 
    #    * @return a newly created {@link UnivariateFunction} that is the value of the line integrand at
    #    *         point t
    #    */
    #   public static UnivariateFunction lineIntegrand(final VectorField field,
    #       final DifferentiableVectorIJKFunction path) {
    #     return new UnivariateFunction() {
    #       @Override
    #       public double evaluate(double t) {
    #         return field.evaluate(path.evaluate(t)).getDot(path.differentiate(t));
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field that is a gradient view of the supplied scalar field.
    #    * 
    #    * @param field a scalar field
    #    * @return a newly created vector field that computes the component-wise gradient of the input
    #    *         field <code> (&#8711;F)</code>
    #    */
    #   public static VectorField gradient(final DifferentiableScalarField field) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         double dfDx = field.differentiateFDi(location);
    #         double dfDy = field.differentiateFDj(location);
    #         double dfDz = field.differentiateFDk(location);
    #         return buffer.setTo(dfDx, dfDy, dfDz);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a vector field that is a curl view of the supplied vector field.
    #    * 
    #    * @param field a vector field
    #    * @return a newly created vector field that computes the component-wise curl of the input field
    #    *         <code> (&#8711; x <b>F</b>)</code>
    #    */
    #   public static VectorField curl(final DifferentiableVectorField field) {
    #     return new VectorField() {
    #       @Override
    #       public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
    #         Results results = field.differentiate(location);
    #         double dFzDy = results.getdFzDy();
    #         double dFyDz = results.getdFyDz();
    #         double dFxDz = results.getdFxDz();
    #         double dFzDx = results.getdFzDx();
    #         double dFyDx = results.getdFyDx();
    #         double dFxDy = results.getdFxDy();
    #         return buffer.setTo(dFzDy - dFyDz, dFxDz - dFzDx, dFyDx - dFxDy);
    #       }
    #     };
    #   }

    #   /**
    #    * Creates a {@link VectorField} that estimates the derivative by utilizing a quadratic
    #    * approximating field over some small, delta interval surrounding the value of interest.
    #    * <p>
    #    * This is the same as simply averaging the forward and backward derivative estimates usually
    #    * utilized to numerically estimate derivatives.
    #    * </p>
    #    * 
    #    * @param field the {@link VectorField} to differentiate numerically
    #    * @param deltaI the delta in the i Cartesian argument to step away from the point of interest in
    #    *        evaluating the derivative
    #    * @param deltaJ the delta in the j Cartesian argument to step away from the point of interest in
    #    *        evaluating the derivative
    #    * @param deltaK the delta in the k Cartesian argument to step away from the point of interest in
    #    *        evaluating the derivative
    #    * @return a newly created {@link DifferentiableVectorField} that differentiates a quadratic
    #    *         approximate to estimate the derivative
    #    */
    #   public static DifferentiableVectorField quadraticApproximation(final VectorField field,
    #       final double deltaI, final double deltaJ, final double deltaK) {
    #     return new QuadraticApproximationDifferentiableVectorField(field, deltaI, deltaJ, deltaK);
    #   }
    # }
