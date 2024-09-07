{-
7. Теоретически возможно, хотя и неэффективно, определить целые числа с помощью рекурсивных типов данных следующим образом:
data Number = Zero | Next Number
Т. е. число является либо нулем (Zero), либо определяется, как число, следующее за предыдущим числом. Например, число 3 записывается как Next (Next (Next Zero)). Определите для такого представления следующие функции:
-}
data Number = Zero | Next Number deriving (Show)
{-
1) fromInt, для заданного целого числа типа Integer возвращающую соответствующее ему значение типа Number.
-}
fromInt :: Integer -> Number
fromInt 0 = Zero
fromInt n = Next (fromInt (n - 1))
{-
fromInt 3
-}

{-
2) toInt, преобразующую значение типа Number в соответствующее целое число.
-}
toInt :: Number -> Integer
toInt Zero = 0
toInt (Next n) = 1 + toInt n
{-
toInt (Next (Next (Next Zero)))
-}

{-
3) plus :: Number -> Number -> Number, складывающую свои аргументы.
-}
plus :: Number -> Number -> Number
plus Zero n = n
plus (Next m) n = Next (plus m n)
{-
plus (fromInt 2) (fromInt 3)
-}

{-
4) mult :: Number -> Number -> Number, умножающую свои аргументы.
-}
mult :: Number -> Number -> Number
mult Zero _ = Zero
mult (Next m) n = plus n (mult m n)
{-
mult (fromInt 2) (fromInt 3)
-}

{-
5) dec, вычитающую единицу из своего аргумента. Для Zero функция должна возвращать Zero.
-}
dec :: Number -> Number
dec Zero = Zero
dec (Next n) = n
{-
dec (fromInt 3)
-}
{-
6) fact, вычисляющую факториал.
-}
fact :: Number -> Number
fact Zero = Next Zero
fact (Next n) = mult (Next n) (fact n)
{-
fact (fromInt 3)
-}