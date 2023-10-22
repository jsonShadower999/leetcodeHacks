  public static String checkstringequal(String s1, String s2) {
        char[] ch1 = s1.toCharArray();
        char[] ch2 = s2.toCharArray();
        int max_len = Math.min(ch1.length, ch2.length);
        String res = "";
        for (int i = 0; i < max_len; i++) {
            if (ch1[i] != ch2[i]) {
                System.out.println(res);
                break;
            } else {
                res = res + ch1[i];
            }

        }
        return res;

    }
