-- CRIAR BANCO DE DADOS
CREATE DATABASE db_amazon;
-- SELECIONAR O BANCO DE DADOS
USE db_amazon;
-- CRIAR TABELA
CREATE TABLE `tb_produtos`(
     -- Define a coluna "id" como um número inteiro, que será incrementado automaticamente a cada novo registro
    -- Também define como PRIMARY KEY, garantindo que cada prato tenha um identificador único
    id INT AUTO_INCREMENT PRIMARY KEY,
      `id` INT PRIMARY KEY AUTO_INCREMENT,
      `nome` VARCHAR(100) NOT NULL,
      `categoria` VARCHAR(100) NOT NULL,
      `preco` DOUBLE NOT NULL
);

-- INSERIR DADOS
INSERT INTO `tb_produtos`(`nome`,`categoria`,`preco`)VALUES
('Pandeiro','Instrumento',22.99),('Fantasia de Princesa','Vestuário',99.90);

  -- PEGANDO DADOS DA TABELA
SELECT * FROM `tb_produtos`;

-- ATUALIZAÇÃO DOS DADOS
UPDATE `tb_produtos`SET `nome` = 'Mascara',`categoria` = 'acessorios',
`preco` = 29.58 WHERE `id` = 1;
-- DELETAR OS DADOS
DELETE FROM `tb_produtos`WHERE `id` = 1;

