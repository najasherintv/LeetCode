SELECT *
FROM Cinema
WHERE id % 2 = 1
   AND deScription != 'boring'
ORDER BY rating DESC;   