{-9-}
{- -----------1---------- -}
{- !!!!!!!!!!!!ВТОРОЙ ПУНКТ ВНИЗУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! -}
{-1-}
{-Список натуральных чисел.-}
first :: Integer -> [Integer]
first 0 = []
first n = first (n-1) ++ [n]
{-enumFromTo 1 n-}
{-2-}
{-Список нечетных натуральных чисел.-}
second :: Integer -> [Integer]
second 0 = []
second n | odd n = second(n-1) ++ [n]
         | otherwise = second (n-1)
{-enumFromThenTo 1 3 n-}
{-3-}
{-Список четных натуральных чисел.-}
third :: Integer -> [Integer]
third 0 = []
third n | even n = third(n-1) ++ [n]
        | otherwise = third (n-1)
{-4-}
{-Список квадратов натуральных чисел.-}
fourth :: Integer -> [Integer]
fourth 0 = []
fourth n = fourth (n-1) ++ [n^2]
{-5-}
{- Список факториалов.-}
f5 :: Integer -> Integer
f5 0 = 1
f5 n = n * f5 (n-1)

fifth :: Integer -> [Integer]
fifth 0 = []
fifth n = fifth (n-1) ++ [f5 n]
{-6-}
{- Список степеней двойки.-}
sixth :: Integer -> [Integer]
sixth 0 = []
sixth n = sixth (n-1) ++ [2^n]
{-7-}
{- Список треугольных чисел 3 .-}
f7 :: Integer -> Integer
f7 0 = 0
f7 n = n * (n+1) `div` 2

seventh :: Integer -> [Integer]
seventh 0 = []
seventh n = seventh (n-1) ++ [f7 n]

{-8-}
{- Список пирамидальных чисел 4 .-}
f8 :: Integer -> Integer
f8 0 = 0
f8 n = n * (n+1) * (n+2) `div` 6

eighth :: Integer -> [Integer]
eighth 0 = []
eighth n = eighth (n-1) ++ [f8 n]
-}
{-  ------------------2----------------  -}
{-3-}
{-3) Функция сложения элементов двух списков. 
Возвращает список, составленный из сумм элементов списков-параметров.
 Учесть, что переданные списки могут быть разной длины.-}
foo :: [Integer] -> [Integer] -> [Integer]
foo [] [] = []
foo [] ys = ys
foo xs [] = xs
foo (x:xs) (y:ys) = (x+y) : foo xs ys
{-foo [1,2,3] [1,2]-}
{-6-}
{- Функция removeOdd, которая удаляет из заданного списка целых чисел все нечетные числа. Например:
removeOdd [1,4,5,6,10] должен возвращать [4,10].         
-}
removeOdd :: [Integer] -> [Integer]
removeOdd [] = []
removeOdd (x:xs) | x == 6 = removeOdd xs  {- [4,6,10]  =)  -}
                 | even x = x : removeOdd xs
                 | otherwise = removeOdd xs

{- removeOdd
foo :: [Integer] -> [Integer]
foo l = helper l [] where
    helper [] a = reverse a
    helper (x:xs) a | even x = helper xs (x:a)
                    | otherwise = helper xs a
-}
