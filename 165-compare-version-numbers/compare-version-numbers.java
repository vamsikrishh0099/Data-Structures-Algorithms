class Solution {
    public int compareVersion(String version1, String version2) {

        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");

        int l = 0;
        int r = 0;

        while (l < v1.length || r < v2.length) {

            String curV1;
            String curV2;
            curV1 = "0";
            curV2 = "0";

            if (l < v1.length) {
                curV1 = v1[l];
            }
            if (r < v2.length) {
                curV2 = v2[r];
            }

            int startl = 0;
            int startr = 0;

            while (startl < curV1.length() && curV1.charAt(startl) == '0') {
                startl++;
            }
            while (startr < curV2.length() && curV2.charAt(startr) == '0') {
                startr++;
            }

            int num1, num2;
            if (startl >= curV1.length()) {
                num1 = 0;
            } else {
                num1 = Integer.parseInt(curV1.substring(startl));
            }

            if (startr >= curV2.length()) {
                num2 = 0;
            } else {
                num2 = Integer.parseInt(curV2.substring(startr));
                

            }

            if (num1 < num2)
                return -1;
            else if (num1 > num2)
                return 1;
            l++;
            r++;

        }

        return 0;

    }
}