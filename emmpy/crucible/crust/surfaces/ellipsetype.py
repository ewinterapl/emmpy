"""emmpy.crucible.crust.surfaces.ellipsetype"""


class EllipseType:
    """Enumeration describing the type of ellipses supported by the Ellipse
    class.

    author F.S.Turner
    """
    POINT = 0
    LINE_SEGMENT = 1
    ELLIPSE = 2

    #     /**
    #     * Indicates the ellipse has both semi-axes with zero length.
    #     */
    #     POINT(true) {
    #     @Override
    #     boolean intersects(UnwritableEllipse ellipse, UnwritablePlane plane) {
    #         checkArgument(ellipse.type == POINT);
    #         /*
    #         * This is simple, determine if the point is contained within the plane.
    #         */
    #         return plane.contains(ellipse.center);
    #     }
    #     @Override
    #     boolean isContainedWithin(UnwritableEllipse ellipse, UnwritablePlane plane) {
    #         checkArgument(ellipse.type == POINT);
    #         /*
    #         * Also simple, just determine if the point is contained with the plane.
    #         */
    #         return plane.contains(ellipse.center);
    #     }
    #     @Override
    #     void intersect(UnwritableEllipse ellipse, UnwritablePlane plane, VectorIJK bufferOne,
    #         VectorIJK bufferTwo) {
    #         checkArgument(ellipse.type == POINT);
    #         checkArgument(isContainedWithin(ellipse, plane),
    #             "Point degenerate ellipse does not intersect plane");
    #         bufferOne.setTo(ellipse.center);
    #         bufferTwo.setTo(ellipse.center);
    #     }
    #     },

    #     /**
    #     * Indicates the ellipse has a semi-minor axes with zero length.
    #     */
    #     LINE_SEGMENT(true) {
    #     @Override
    #     boolean intersects(UnwritableEllipse ellipse, UnwritablePlane plane) {
    #         checkArgument(ellipse.type == LINE_SEGMENT);
    #         /*
    #         * First get the entire containment case out of the way.
    #         */
    #         if (isContainedWithin(ellipse, plane)) {
    #         return true;
    #         }
    #         /*
    #         * Compute the plane constant after translating the origin so that it is at the ellipse's
    #         * center.
    #         */
    #         VectorIJK recenteredOrigin =
    #             VectorIJK.combine(plane.getConstant(), plane.normal, -1.0, ellipse.center);
    #         double recenteredConstant = Math.abs(plane.normal.getDot(recenteredOrigin));
    #         return Math.abs(ellipse.smajor.getDot(plane.normal)) >= recenteredConstant;
    #     }
    #     @Override
    #     boolean isContainedWithin(UnwritableEllipse ellipse, UnwritablePlane plane) {
    #         checkArgument(ellipse.type == LINE_SEGMENT);
    #         /*
    #         * Determine if the center is contained within the plane.
    #         */
    #         if (!plane.contains(ellipse.center)) {
    #         return false;
    #         }
    #         /*
    #         * Check that the semi-major axes is orthogonal to the the plane's normal.
    #         */
    #         return ellipse.smajor.getDot(plane.normal) == 0;
    #     }
    #     @Override
    #     void intersect(UnwritableEllipse ellipse, UnwritablePlane plane, VectorIJK bufferOne,
    #         VectorIJK bufferTwo) {
    #         checkArgument(ellipse.type == LINE_SEGMENT);
    #         /*
    #         * Verify that the line segment is not completely contained within the plane.
    #         */
    #         checkArgument(!isContainedWithin(ellipse, plane),
    #             "Line segment degenerate ellipse is entirely " + "contained within the plane");
    #         /*
    #         * We will handle the case of no intersection as we go forward. While we could utilize the
    #         * intersects() method on this type, it would result in redundant execution. Create a new
    #         * plane that is just the supplied plane recentered to the center of the ellipse.
    #         */
    #         VectorIJK newCenter =
    #             VectorIJK.combine(plane.getConstant(), plane.normal, -1.0, ellipse.center);
    #         Plane newPlane = new Plane(plane.normal, newCenter);
    #         double v = ellipse.smajor.getDot(newPlane.normal);
    #         double absV = Math.abs(v);
    #         /*
    #         * Check to see if there is no intersection. This is two parts, first if the line segment is
    #         * parallel to the plane (v == 0) or if Math.abs(v) < newPlane.getConstant.
    #         */
    #         checkArgument(v != 0, "Line segment degenerate ellipse is parallel to"
    #             + " the candidate plane for intersection");
    #         checkArgument(absV >= newPlane.getConstant(), "Line segment degenerate ellipse does not "
    #             + "intersect the candidate plane.");
    #         /*
    #         * The sign of the scale for the semi-major axis should be the same sign as v.
    #         */
    #         VectorIJK.combine(1.0, ellipse.center, Math.signum(v) * newPlane.getConstant() / absV,
    #             ellipse.smajor, bufferOne);
    #         bufferTwo.setTo(bufferOne);
    #     }
    #     },

    #     /**
    #     * Indicates the ellipse has a semi-axes with non-zero length.
    #     */
    #     ELLIPSE(false) {
    #     @Override
    #     boolean intersects(UnwritableEllipse ellipse, UnwritablePlane plane) {
    #         checkArgument(ellipse.type == ELLIPSE);
    #         /*
    #         * First get the entire containment case out of the way.
    #         */
    #         if (isContainedWithin(ellipse, plane)) {
    #         return true;
    #         }
    #         /*
    #         * Compute the plane constant after translating the origin so that it is at the ellipse's
    #         * center.
    #         */
    #         VectorIJK recenteredOrigin =
    #             VectorIJK.combine(plane.getConstant(), plane.normal, -1.0, ellipse.center);
    #         double recenteredConstant = Math.abs(plane.normal.getDot(recenteredOrigin));
    #         double v1 = ellipse.smajor.getDot(plane.normal);
    #         double v2 = ellipse.sminor.getDot(plane.normal);
    #         return Math.hypot(v1, v2) >= recenteredConstant;
    #     }
    #     @Override
    #     boolean isContainedWithin(UnwritableEllipse ellipse, UnwritablePlane plane) {
    #         checkArgument(ellipse.type == ELLIPSE);
    #         /*
    #         * Determine if the center is contained within the plane.
    #         */
    #         if (!plane.contains(ellipse.center)) {
    #         return false;
    #         }
    #         /*
    #         * Verify that both semi-axes are orthogonal to the plane's normal.
    #         */
    #         return ((ellipse.smajor.getDot(plane.normal) == 0) && (ellipse.sminor.getDot(plane.normal) == 0));
    #     }
    #     @Override
    #     void intersect(UnwritableEllipse ellipse, UnwritablePlane plane, VectorIJK bufferOne,
    #         VectorIJK bufferTwo) {
    #         checkArgument(ellipse.type == ELLIPSE);
    #         /*
    #         * Verify that the line segment is not completely contained within the plane.
    #         */
    #         checkArgument(!isContainedWithin(ellipse, plane),
    #             "Ellipse is entirely contained within the plane");
    #         /*
    #         * We will handle the case of no intersection as we go forward. While we could utilize the
    #         * intersects() method on this type, it would result in redundant execution. Create a new
    #         * plane that is just the supplied plane recentered to the center of the ellipse.
    #         */
    #         VectorIJK newCenter =
    #             VectorIJK.combine(plane.getConstant(), plane.normal, -1.0, ellipse.center);
    #         Plane newPlane = new Plane(plane.normal, newCenter);
    #         double v1 = ellipse.smajor.getDot(newPlane.normal);
    #         double v2 = ellipse.sminor.getDot(newPlane.normal);
    #         double vnorm = Math.hypot(v1, v2);
    #         /*
    #         * Check to see if there is no intersection. This is two parts, first if the line segment is
    #         * parallel to the plane (v == 0) or if Math.abs(v) < newPlane.getConstant.
    #         */
    #         checkArgument((v1 != 0.0) || (v2 != 0.0),
    #             "Ellipse is parallel to the candidate plane for intersection");
    #         checkArgument(vnorm >= newPlane.getConstant(),
    #             "Ellipse does not intersect the candidate plane");
    #         double alpha = Math.acos(newPlane.getConstant() / vnorm);
    #         double beta = Math.atan2(v2, v1);
    #         double angle1 = beta - alpha;
    #         double angle2 = beta + alpha;
    #         VectorIJK.combine(1.0, ellipse.center, Math.cos(angle1), ellipse.smajor, Math.sin(angle1),
    #             ellipse.sminor, bufferOne);
    #         VectorIJK.combine(1.0, ellipse.center, Math.cos(angle2), ellipse.smajor, Math.sin(angle2),
    #             ellipse.sminor, bufferTwo);
    #     }
    #     };

    #     /**
    #     * Field indicating whether the ellipse type is degenerate.
    #     */
    #     private final boolean degenerate;

    #     /**
    #     * Constructs the instance with the given degeneracy.
    #     * 
    #     * @param degenerate is the type degenerate?
    #     */
    #     private Type(boolean degenerate) {
    #     this.degenerate = degenerate;
    #     }

    #     /**
    #     * Indicates whether the type is degenerate or not.
    #     * 
    #     * @return true if degenerate, false otherwise.
    #     */
    #     public boolean isDegenerate() {
    #     return degenerate;
    #     }

    #     /**
    #     * Package private method that determines whether the ellipse of a particular type intersects a
    #     * plane.
    #     * <p>
    #     * Designed to support {@link UnwritableEllipse#intersects(UnwritablePlane)}
    #     * </p>
    #     * 
    #     * @param ellipse the ellipse
    #     * @param plane the plane
    #     * 
    #     * @return true if ellipse and plane intersect, false otherwise
    #     */
    #     abstract boolean intersects(UnwritableEllipse ellipse, UnwritablePlane plane);

    #     /**
    #     * Package private method that determines whether the ellipse of a particular type is completely
    #     * contained within a plane.
    #     * <p>
    #     * Designed to support {@link UnwritableEllipse#isContainedWithin(UnwritablePlane)}
    #     * </p>
    #     * 
    #     * @param ellipse the ellipse
    #     * @param plane the plane
    #     * 
    #     * @return true if plane completely contains ellipse, false otherwise
    #     */
    #     abstract boolean isContainedWithin(UnwritableEllipse ellipse, UnwritablePlane plane);

    #     /**
    #     * Computes the intersection points of an ellipse of a particular type with a plane.
    #     * <p>
    #     * Designed to support
    #     * {@link UnwritableEllipse#intersect(UnwritablePlane, VectorIJK, VectorIJK)}
    #     * </p>
    #     * 
    #     * @param ellipse the ellipse
    #     * @param plane the plane
    #     * @param bufferOne buffer to capture the an intersection point
    #     * @param bufferTwo another, separate buffer, to capture another intersection point
    #     * 
    #     * @throws IllegalArgumentException if there are no intersections or if the ellipse is
    #     *         completely contained within the plane. To guard against this use:
    #     *         {@link UnwritableEllipse#isContainedWithin(UnwritablePlane)} and
    #     *         {@link UnwritableEllipse#intersects(UnwritablePlane)}
    #     */
    #     abstract void intersect(UnwritableEllipse ellipse, UnwritablePlane plane, VectorIJK bufferOne,
    #         VectorIJK bufferTwo);
    # };
