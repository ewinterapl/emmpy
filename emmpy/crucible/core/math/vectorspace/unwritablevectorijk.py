class UnwritableVectorIJK:

    def __init__(self, *args):
        if len(args) == 1:
            # List or tuple of >=3 doubles
            if isinstance(args[0], (list, tuple)):
                self.i = args[0][0]
                self.j = args[0][1]
                self.k = args[0][2]
            # Copy constructor
            elif isinstance(args[0], UnwritableVectorIJK):
                self.i = args[0].i
                self.j = args[0].j
                self.k = args[0].k
            else:
                # Throw exception
                pass
        elif len(args) == 2:
            # Offset and array of >=3 doubles
            # Copy and scale
            pass
        elif len(args) == 3:
            # 3 numbers
            self.i = args[0]
            self.j = args[1]
            self.k = args[2]
        else:
            # Throw exception
            pass

        # createUnitized()
        # createNegated()
        # createScaled()
        # getI()
        # getJ()
        # getK()
        # get(i)
        # getLength()
        # getDot()
        # getSeparation()
        # getSeparationOutOfPlane()
        # copyOf()
        # hashCode()
        # equals()
        # toString()

if __name__ == '__main__':
    v = UnwritableVectorIJK([1, 2, 3])
    # self.assertEqual(v.i, 1.0)
    # self.assertEqual(v.j, 2.0)
    # self.assertEqual(v.k, 3.0)
