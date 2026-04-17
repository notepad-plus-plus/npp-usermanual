---
weight: 83
title: UDL > Folding in code
slug: folding-in-code
---

# UDL &gt; Folding in code

Folding in code is quite different in UDL 2.1. Instead of two keyword sets (open and close), now we have three keyword sets (**open**, **middle** and **close**). Also, there are two Folding in code  groups: one for [forward (style1)](../introduction/) and one for [backward (style2)](../introduction/) search.

The **open** field is used for the keyword(s) or symbol(s) that indicate the start of a folding block; the **close** field is used for the keyword(s) or symbol(s) that indicate the end of the folding block; the **middle** allows ending one block and starting the next (at the same level) with a single keyword (and is used for things like the `else-if` and `else` blocks in an `if`/`else-if`/`else`/`end-if` sequence).  

If you define both an **open** and a **close**, then you can do arbitrary nesting of folding-inside-folding. 

Under most circumstances, it does not make sense to have an `else` without a starting `if`, so the UDL folding processing was designed to have **middle** function correctly when there is an **open** before it; if **open** has not defined any keywords or symbols, or if the UDL parses the file and finds a **middle** keyword not preceded by an **open** keyword, then it may have a fold indicator at the **middle**, but there may be unexpected side effects: if you want to make sure **middle** folding works as expected, make sure to use an **open** keyword before it.

## Example 1

This is a typical C++ folding definition.<br>
Curly braces represent folding points in the code and preprocessor is also supported (for this demo not all statements were defined)

![](../images/folding_in_code_01.png)

There are two important things here.<br>
As you can see both Folding 1 and Folding 2 create folding points, but they work differently.

- Folding 1 (the curly braces) is detected using forward search. It means these keywords can be "glued" to some other keyword. In this case opening curly brace stands next to closing round brace, and in line 12 around word `int`
- Folding 2 (preprocessor stuff) works when surrounded by white space, but not when glued to word `UNICODE`, as demonstrated in line 14

![](../images/folding_in_code_02.png)

Note: forward and backward search concept is explained in more detail in the [UDL Parser](../introduction/) page.<br>
You should read that part if you haven't already.

## Example 2

UDL 2.1 will automatically create middle folding point if open folding point is followed by a close folding point on the same line.

![](../images/folding_in_code_03.png)

## Example 3

Use of multi-part keywords is supported in Folder in code 2, as you can see in this example.

![](../images/folding_in_code_04.png)

{{< radic >}}
