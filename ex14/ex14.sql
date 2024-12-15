-- 14. Escreva uma consulta SQL que calcule a média de idade dos clientes cujo email termina em "@example.com".

SELECT 
    AVG(idade) AS media_idade -- calcula a media da coluna idade com avg
FROM 
    clientes
WHERE 
    email LIKE '%@example.com'; -- filtra apenas os clientes com o email que termina com @example.com
