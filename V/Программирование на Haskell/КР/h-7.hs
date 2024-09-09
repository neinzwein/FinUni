{-
Дервук Максим А. ЗБ-ПИ20-1
-}
{-
14. Определить, является ли список геометрической прогрессией
-}

foo1 :: (Eq a, Fractional a) => [a] -> Bool
foo1 []  = True
foo1 [_] = True
foo1 (x:y:xs) | x == 0    = False
              | otherwise = all (\(a, b) -> b * ratio == a) (zip xs (y:xs))
  where ratio = y / x

{-
foo1 [2,4,8,16]
foo1 [1,2,4,7]
-}