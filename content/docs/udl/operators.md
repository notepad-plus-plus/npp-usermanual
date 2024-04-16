---
weight: 88
title: UDL > Operators
---

# Operators

This section gives short explanation of operator options.<br>
For detailed discussion about "forward" and "backward" search, please read section [Introduction]({{ site.baseurl }}/introduction/).

![Operators dialog](../images/operators_01.png)

Operators are split into two groups: Operators1 and Operators2.

## Operators1

This is a "forward" search group.<br>
These operators can be "glued" to other keywords. You can use it to define operators like:

```
! && << >> + - _ %
```

In short: these should be special non-alphanumeric characters

## Operators2

This is a "backward" search group.<br>
These operators can NOT be "glued" to other keywords. They must be separated from rest of the code by whitespace or by other "forward" search keywords.You can use it to define operators like:

```
and or not in out like
```

In short: operators that look like keywords

Operators2 group is just another keyword group, Keyword group 9 if you will. I added it here just for easier use of UDL 2.1 GUI, and for better understanding of how operators work. Users could define the same keyword list in keywords groups 1 through 8 and there would be no difference.

![Operators example 1](../images/operators_02.png)

As demonstrated in picture above, Operators1 are always highlighted, and Operators2 are highlighted only if separated from rest of the code.

{{< radic >}}
