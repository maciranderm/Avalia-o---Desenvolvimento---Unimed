-- 13. Descreva como você faria para obter uma lista de todos os clientes e suas respectivas ordens (assuma que há uma tabela "Ordens" relacionada com a tabela "Clientes" via chave estrangeira). Inclua clientes que não têm ordens.

-- seleciona os dados dos clientes e suas ordens
SELECT 
    c.id_cliente,
    c.nome_cliente,
    o.id_ordem,
    o.valor_ordem
FROM 
    clientes c -- define a tab clientes como a principal
LEFT JOIN 
    ordens o -- faz um LEFT JOIN para incluir os dados da tabela ordens, pois devo incluir clientes que nao possuem ordens
ON 
    c.id_cliente = o.id_cliente  -- relaciona as tabelas pelo id_cliente como chave
ORDER BY
    c.nome_cliente; -- optei por ordernar o resultado pelo nome do cliente em ordem alfabetica para ficar mais organizada a visualizacao

    
