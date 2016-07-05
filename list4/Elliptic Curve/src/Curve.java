import java.math.BigInteger;
import java.util.ArrayList;

public class Curve {

	public static final Point inf = new Point(0, 0);
	public static final BigInteger ONE = BigInteger.ONE, TWO = BigInteger
			.valueOf(2), THREE = BigInteger.valueOf(3);

	public int a, b, modp;
	public BigInteger modP;

	public Curve(int a, int b, int p) {
		this.a = a;
		this.b = b;
		modp = p;
		modP = BigInteger.valueOf(modp);
	}

	public int findOrder(Point p) {

		int order = 1;
		Point result = p;

		while (!result.equals(inf)) {
			result = addition(p, result);
			order++;
		}

		return order;
	}

	public ArrayList<Point> findAllPoints() {

		ArrayList<Point> results = new ArrayList<Point>();

		int[] roots;

		for (int x = 0; x < modp; x++) {
			roots = squareRoot(f(x));

			if (roots != null) {
				results.add(new Point(x, roots[0]));

				if (roots[0] != roots[1])
					results.add(new Point(x, roots[1]));
			}
		}
		
		results.add(inf);

		return results;
	}

	public int f(int x) {
		return (BigInteger.valueOf(x).modPow(THREE, modP)
				.intValue()
				+ BigInteger.valueOf(a).multiply(BigInteger.valueOf(x))
						.mod(modP).intValue() + b)
				% modp;
	}

	public int[] squareRoot(int y) {

		int x = BigInteger.valueOf(y)
				.modPow(BigInteger.valueOf((modp + 1) / 4), modP).intValue();

		if ((x * x) % modp == y)
			return new int[] { x, (modp - x) % modp };
		else
			return null;
	}

	public Point addition(Point p, Point q) {

		if (p.equals(inf)) {
			return q;
		}
		if (q.equals(inf)) {
			return p;
		}
		if (p.x == q.x && p.y == (-q.y + modp) % modp) {
			return inf;
		}

		int lambda;
		BigInteger l;

		if (!p.equals(q)) {

			lambda = (p.y - q.y) % modp;
			if (lambda < 0)
				lambda += modp;

			l = BigInteger.valueOf(lambda);

			lambda = modInverse(p.x - q.x).multiply(l).mod(modP).intValue();

		} else {

			lambda = modInverse(2 * p.y)
					.multiply(
							BigInteger.valueOf(p.x).modPow(TWO, modP)
									.multiply(THREE).add(BigInteger.valueOf(a)))
					.mod(modP).intValue();
		}

		l = BigInteger.valueOf(lambda);

		int xr = (l.modPow(TWO, modP).intValue() - (p.x + q.x)) % modp;
		if (xr < 0)
			xr += modp;
		int yr = (l.multiply(BigInteger.valueOf(p.x - xr)).mod(modP).intValue() - p.y)
				% modp;
		if (yr < 0)
			yr += modp;

		return new Point(xr, yr);
	}

	public BigInteger modInverse(int a) {
		return BigInteger.valueOf(a).modInverse(modP);
	}

}