-- 12. Escreva uma consulta SQL para selecionar todos os registros da tabela "Clientes" onde o nome começa com a letra "A".

SELECT * FROM clientes -- seleciona os registros da tab. clientes
WHERE nome LIKE 'A%'; -- filtra apenas os registros que comeca com A
