"""A quadratic approximation of a differentiable vector field.

Authors
-------
G.K. Stephens
Eric Winter (eric.winter@jhuapl.edu)
"""


# Import project modules.
from emmpy.math.vectorfields.differentiablevectorfield import (
    DifferentiableVectorField
)


class QuadraticApproximationDifferentiableVectorField(DifferentiableVectorField):
    """A quadratic approximation of a differentiable vector field.

    Attributes
    ----------
    field : VectorField
        Vector field to differentiate.
    deltaI, deltaJ, deltaK : float
        Differential distances along each dimension, for computing numerical
        derivatives.
    """

    def __init__(self, field, deltaI, deltaJ, deltaK):
        """Initialize a new object.

        Parameters
        ----------
        field : VectorField
            Vector field to differentiate.
        deltaI, deltaJ, deltaK : float
            Differential distances along each dimension, for computing
            numerical derivatives.

        Returns
        -------
        None
        """
        self.field = field
        self.deltaI = deltaI
        self.deltaJ = deltaJ
        self.deltaK = deltaK

# class QuadraticApproximationDifferentiableVectorField implements DifferentiableVectorField {

#   private final VectorField field;

#   private final double deltaI;
#   private final double deltaJ;
#   private final double deltaK;

#   public QuadraticApproximationDifferentiableVectorField(VectorField field, double deltaI,
#       double deltaJ, double deltaK) {

#     this.field = checkNotNull(field);
#     checkArgument(deltaI > 0.0 && deltaJ > 0.0 && deltaK > 0.0);

#     this.deltaI = deltaI;
#     this.deltaJ = deltaJ;
#     this.deltaK = deltaK;
#   }

#   @Override
#   public double differentiateFiDi(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i + deltaI, j, k);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i - deltaI, j, k);

#     return 0.5 / deltaI * (field.evaluate(add).getI() - field.evaluate(sub).getI());
#   }

#   @Override
#   public double differentiateFjDi(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i + deltaI, j, k);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i - deltaI, j, k);

#     return 0.5 / deltaI * (field.evaluate(add).getJ() - field.evaluate(sub).getJ());
#   }

#   @Override
#   public double differentiateFkDi(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i + deltaI, j, k);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i - deltaI, j, k);

#     return 0.5 / deltaI * (field.evaluate(add).getK() - field.evaluate(sub).getK());
#   }

#   @Override
#   public double differentiateFiDj(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i, j + deltaJ, k);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i, j - deltaJ, k);

#     return 0.5 / deltaJ * (field.evaluate(add).getI() - field.evaluate(sub).getI());
#   }

#   @Override
#   public double differentiateFjDj(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i, j + deltaJ, k);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i, j - deltaJ, k);

#     return 0.5 / deltaJ * (field.evaluate(add).getJ() - field.evaluate(sub).getJ());
#   }

#   @Override
#   public double differentiateFkDj(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i, j + deltaJ, k);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i, j - deltaJ, k);

#     return 0.5 / deltaJ * (field.evaluate(add).getK() - field.evaluate(sub).getK());
#   }

#   @Override
#   public double differentiateFiDk(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i, j, k + deltaK);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i, j, k - deltaK);

#     return 0.5 / deltaK * (field.evaluate(add).getI() - field.evaluate(sub).getI());
#   }

#   @Override
#   public double differentiateFjDk(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i, j, k + deltaK);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i, j, k - deltaK);

#     return 0.5 / deltaK * (field.evaluate(add).getJ() - field.evaluate(sub).getJ());
#   }

#   @Override
#   public double differentiateFkDk(UnwritableVectorIJK location) {
#     double i = location.getI();
#     double j = location.getJ();
#     double k = location.getK();

#     UnwritableVectorIJK add = new UnwritableVectorIJK(i, j, k + deltaK);
#     UnwritableVectorIJK sub = new UnwritableVectorIJK(i, j, k - deltaK);

#     return 0.5 / deltaK * (field.evaluate(add).getK() - field.evaluate(sub).getK());
#   }

#   @Override
#   public VectorIJK evaluate(UnwritableVectorIJK location, VectorIJK buffer) {
#     return field.evaluate(location, buffer);
#   }

#   @Override
#   public Results differentiate(UnwritableVectorIJK location) {

#     double x = location.getI();
#     double y = location.getJ();
#     double z = location.getK();

#     UnwritableVectorIJK f = field.evaluate(location);

#     UnwritableVectorIJK addX = new UnwritableVectorIJK(x + deltaI, y, z);
#     UnwritableVectorIJK subX = new UnwritableVectorIJK(x - deltaI, y, z);

#     UnwritableVectorIJK addY = new UnwritableVectorIJK(x, y + deltaJ, z);
#     UnwritableVectorIJK subY = new UnwritableVectorIJK(x, y - deltaJ, z);

#     UnwritableVectorIJK addZ = new UnwritableVectorIJK(x, y, z + deltaK);
#     UnwritableVectorIJK subZ = new UnwritableVectorIJK(x, y, z - deltaK);

#     UnwritableVectorIJK fieldAddX = field.evaluate(addX);
#     UnwritableVectorIJK fieldSubX = field.evaluate(subX);

#     UnwritableVectorIJK fieldAddY = field.evaluate(addY);
#     UnwritableVectorIJK fieldSubY = field.evaluate(subY);

#     UnwritableVectorIJK fieldAddZ = field.evaluate(addZ);
#     UnwritableVectorIJK fieldSubZ = field.evaluate(subZ);

#     double dFxDx = 0.5 / deltaI * (fieldAddX.getI() - fieldSubX.getI());
#     double dFyDx = 0.5 / deltaI * (fieldAddX.getJ() - fieldSubX.getJ());
#     double dFzDx = 0.5 / deltaI * (fieldAddX.getK() - fieldSubX.getK());

#     double dFxDy = 0.5 / deltaJ * (fieldAddY.getI() - fieldSubY.getI());
#     double dFyDy = 0.5 / deltaJ * (fieldAddY.getJ() - fieldSubY.getJ());
#     double dFzDy = 0.5 / deltaJ * (fieldAddY.getK() - fieldSubY.getK());

#     double dFxDz = 0.5 / deltaK * (fieldAddZ.getI() - fieldSubZ.getI());
#     double dFyDz = 0.5 / deltaK * (fieldAddZ.getJ() - fieldSubZ.getJ());
#     double dFzDz = 0.5 / deltaK * (fieldAddZ.getK() - fieldSubZ.getK());

#     Results results = new Results(f, dFxDx, dFxDy, dFxDz, dFyDx, dFyDy, dFyDz, dFzDx, dFzDy, dFzDz);

#     return results;
#   }

# }
