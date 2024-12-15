-- 15. Explique como você atualizaria o email de um cliente específico na tabela "Clientes", onde o ID do cliente é conhecido.

-- daria um where para selecionar o cliente especificado e atualizar a informacao dele

UPDATE clientes
SET email = 'unimed@exemplo.com'
WHERE cliente_id = 5001;   -- para que apenas o cliente especifico seja atualizado
