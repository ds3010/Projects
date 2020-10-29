public class Doubles {
    public static void main(String[] args) {
        double max = Double.MAX_VALUE;
        double min = Double.MIN_NORMAL;
        double max_inf = Double.POSITIVE_INFINITY;
        double min_inf = Double.NEGATIVE_INFINITY;
        double nan = Double.NaN;
        String maxD = Double.toString(max);
        String minD = Double.toString(min);
        String maxinfD = Double.toString(max_inf);
        String mininfD = Double.toString(min_inf);
        String nanD = Double.toString(nan);
        System.out.println("Max Double Value Available: " + maxD);
        System.out.println("Min Double Value Available: " + minD);
        System.out.println("Max Infinite Double Value Available: " + maxinfD);
        System.out.println("Min Infinite Double Value Available: " + mininfD);
        System.out.println("NaN Double Value Available: " + nanD);
    }
}
