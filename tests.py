from Point import Point
import unittest


class TestPointClass(unittest.TestCase):
    def test_add(self):
        p1 = Point(x=1, y=3)
        p2 = Point(x=2, y=4)

        t1 = p1 + p2

        self.assertEqual(t1, Point(x=3, y=7))

        t2 = p1 + 2

        self.assertEqual(t2, Point(x=3, y=5))

        t3 = p1 + 2.2

        self.assertEqual(t3, Point(x=3.2, y=5.2))

    def test_sub(self):
        p1 = Point(x=1, y=3)
        p2 = Point(x=2, y=4)

        t1 = p1 - p2

        self.assertEqual(t1, Point(x=-1, y=-1))

        t2 = p1 - 2

        self.assertEqual(t2, Point(x=-1, y=1))

        t3 = p1 - 2.2

        self.assertAlmostEqual(t3.x, p1.x - 2.2)
        self.assertAlmostEqual(t3.y, p1.y - 2.2)

    def test_negation(self):
        p1 = Point(x=1, y=3)

        self.assertEqual(-p1, Point(x=-1, y=-3))

    def test_mult(self):
        p1 = Point(x=1, y=3)
        p2 = Point(x=2, y=4)

        t1 = p1 * p2

        self.assertEqual(t1, Point(x=2, y=12))

        t2 = p1 * 2

        self.assertEqual(t2, Point(x=2, y=6))

        t3 = p1 * 2.2

        self.assertAlmostEqual(t3.x, p1.x * 2.2)
        self.assertAlmostEqual(t3.y, p1.y * 2.2)

    def test_truediv(self):
        p1 = Point(x=1, y=3)
        p2 = Point(x=2, y=4)

        t1 = p1 / p2

        self.assertAlmostEqual(t1.x, p1.x / p2.x)
        self.assertAlmostEqual(t1.y, p1.y / p2.y)

        t2 = p1 / 2

        self.assertAlmostEqual(t2.x, p1.x / 2)
        self.assertAlmostEqual(t2.y, p1.y / 2)

        t3 = p1 / 2.2

        self.assertAlmostEqual(t3.x, p1.x / 2.2)
        self.assertAlmostEqual(t3.y, p1.y / 2.2)

    def test_floordiv(self):
        p1 = Point(x=1, y=3)
        p2 = Point(x=2, y=4)

        t1 = p1 // p2

        self.assertAlmostEqual(t1.x, p1.x // p2.x)
        self.assertAlmostEqual(t1.y, p1.y // p2.y)

        t2 = p1 // 2

        self.assertAlmostEqual(t2.x, p1.x // 2)
        self.assertAlmostEqual(t2.y, p1.y // 2)

        t3 = p1 // 2.2

        self.assertAlmostEqual(t3.x, p1.x // 2.2)
        self.assertAlmostEqual(t3.y, p1.y // 2.2)

    def test_inversion(self):
        p1 = Point(x=-1, y=4)

        self.assertEqual(~p1, Point(x=4, y=-1))

    def test_magnitude(self):
        p1 = Point(x=4, y=6)

        self.assertAlmostEqual(p1.magnitude(), 7.21110255093)

    def test_degrees(self):
        p1 = Point(x=1, y=0)

        self.assertAlmostEqual(p1.degrees(), 0)

        p2 = Point(x=0, y=1)

        self.assertAlmostEqual(p2.degrees(), 90)

        p3 = Point(x=1, y=1)

        self.assertAlmostEqual(p3.degrees(), 45)

    def test_radians(self):
        p1 = Point(x=1, y=0)

        self.assertAlmostEqual(p1.radians(), 0)

        p2 = Point(x=0, y=1)

        self.assertAlmostEqual(p2.radians(), 1.57079632679)

        p3 = Point(x=1, y=1)

        self.assertAlmostEqual(p3.radians(), 0.78539816339)

    def test_sort(self):
        points = [
            Point(x=2, y=3),
            Point(x=-1, y=0),
            Point(x=0, y=1),
            Point(x=4, y=3),
            Point(x=9, y=0),
            Point(x=1, y=0),
        ]

        sorted_points = sorted(points)

        self.assertEqual(
            sorted_points,
            [
                Point(x=1, y=0),
                Point(x=0, y=1),
                Point(x=-1, y=0),
                Point(x=2, y=3),
                Point(x=4, y=3),
                Point(x=9, y=0),
            ],
        )

    def test_equality(self):
        p1 = Point(x=3, y=1)
        p2 = Point(x=3, y=1)

        self.assertTrue(p1 == p2)

        p3 = Point(x=1, y=3)

        self.assertFalse(p1 == p3)

    def test_setters(self):
        p1 = Point(x=1, y=3)

        p1.set_x(3)

        self.assertEqual(p1, Point(x=3, y=3))

        p1.set_y(4)

        self.assertEqual(p1, Point(x=3, y=4))

        p1.set_point((5, 5))

        self.assertEqual(p1, Point(x=5, y=5))


if __name__ == "__main__":
    unittest.main()
