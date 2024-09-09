{-
Дервук Максим А. ЗБ-ПИ20-1
-}
{-
26. Переставить минимальный элемент списка на первое место
-}

foo2 :: Ord a => [a] -> [a]
foo2 [] = []
foo2 xs = let minElem = minimum xs
              (before, minAndAfter) = break (== minElem) xs
          in minElem : before ++ tail minAndAfter

{-
moveMinToFront [3,10,1,2,5]
moveMinToFront [1,2,3,4,5]
-}