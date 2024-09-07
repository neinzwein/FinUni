{- removeOdd :: [a] -> [a] -}

{-
removeOdd l = remove a b where
    a = l
    b = []
    remove a b = if (even head a == True) then (b : (head a)) else removeOdd (tail a)
-}

{-
removeOdd :: [Integer] -> [Integer]
removeOdd [] = []
removeOdd (x:xs) = helper x xs where
  helper x [] = if even x then [x] else []
  helper x (y:ys) = if even x then x : helper y ys else helper y ys
-}
{-
foo :: [Integer] -> [Integer]
foo l = helper l [] where
    helper [] a = reverse a
    helper (x:xs) a | even x = helper xs (x:a)
                    | otherwise = helper xs a
-}
{-
import Data.Char
delAllUpper :: String -> String
delAllUpper x = helper (words x) [] where
    helper [] y = unwords (y)
    helper (x:xs) y | all (isUpper) x = helper xs y
                    | otherwise = helper xs (y ++ [x])
-}
{-
GHCi> perms [1,2,3]
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
-}
{-
max3 :: Ord a => [a] -> [a] -> [a] -> [a]

max3 [] [] [] = []
max3 (x:xs) (y:ys) (z:zs) = maximum [x,y,z] : max3 (xs) (ys) (zs)
-} 
{-
GHCi> max3 [7,2,9] [3,6,8] [1,8,10]
[7,8,10]
GHCi> max3 "AXZ" "YDW" "MLK"
"YXZ"
-}
{-
perms :: [a] -> [[a]]
perms [] = [[]]
perms (x:xs) = helper x (perms xs)
  where
    helper :: a -> [[a]] -> [[a]]
    helper x = concatMap (helper' x)
    
    helper' :: a -> [a] -> [[a]]
    helper' x [] = [[x]]
    helper' x (y:ys) = (x:y:ys) : map (y:) (helper' x ys)
-}