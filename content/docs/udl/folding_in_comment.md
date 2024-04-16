---
weight: 84
title: UDL > Folding in comment
slug: folding-in-comment
---

# Folding in comment

This keyword set is new in UDL 2.1.<br>
It allows you to fold anything as long as your language supports comments.<br>
Let's demonstrate it by using C++ comments.

## Example 1

![](../images/folding_in_comment_01.png)

Note: When selecting keywords that turn comments into folding points, it is important to select unique keywords. Don't use stuff that is part of your source code, that will create unexpected folding points when you comment out parts of your source code.

![](../images/folding_in_comment_02.png)

Notice how comments that have "folding in comment" keywords embedded in them, create folding points in your code. I even mixed line comments and normal comments, and it works. So, any comment with "folding in comment" keywords embedded can become a folding point. And remember, these are just comments, you can put them anywhere you like. In fact, you can use this feature to organize your code. For one way to do it, see next example.

## Example 2

Let's steal some ideas from C#. Our code will be organized in "regions".

![](../images/folding_in_comment_03.png)

One keyword group will be anything that starts with "at sign" `@`, so check Prefix mode option.

![](../images/folding_in_comment_04.png)

We'll define comments as standard C++ comments:

```
/* cpp comment */
// cpp line comment
```

The important thing here is to allow nesting of keyword group two (words that start with `@` sign)

![](../images/folding_in_comment_05.png)

Finally, the magic happens.<br>
I organized my code in three logical groups:

- initialization
- execution
- clean up

These three keywords are not defined anywhere, I can call my regions anything I like, as long as I use `@` prefix.

Notice how `region` and `end` keywords have the same color as comments, but `@region_name` uses distinct color to be easily noticeable.

![](../images/folding_in_comment_06.png)

Folding in comment keywords support multi-part keywords too.

In the end, I would just like to say that, if used properly, this could be the single most useful feature of UDL 2.1.

{{< radic >}}
