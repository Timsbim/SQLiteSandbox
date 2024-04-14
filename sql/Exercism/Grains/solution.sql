UPDATE grains
SET result = CASE task
        WHEN 'single-square' THEN power(2, square - 1)
        ELSE power(2, 64) - 1
    END;
