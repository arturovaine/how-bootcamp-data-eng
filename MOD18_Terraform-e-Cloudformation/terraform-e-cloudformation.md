IAC: Infrastructure As Code (Estrutura por código)

Motivação: 

- Mitigar riscos através de realização de testes;
- Garantir que as configurações estão aplicadas de maneira homogênea;
- Ter os mesmos ambientes desde a máquina do desenvolvedor até o ambiente de produção;
- Utilizar os recursos de maneira eficiente através do uso de ambientes temporários;
- Ter todo o histórico das alterações realizadas no ambiente

Fonte: SempreUpdate

# Introdução ao AWS Cloudformation

- Cloudformation: pilhas e templates

"Um modelo do Cloudformation descreve os recursos desejados e suas dependências para que voce possa iniciá-los e configurá-los em conjunto como uma pilha. Você pode usar um modelo para criar, atualizar e excluir uma pilha inteira como uma única unidade, quantas vezes quiser, em vez de gerenciar os recursos individualmente. As pilhas podem ser gerenciadas e provisionadas em várias contas e regiões da AWS."

<br>

## Templates e stacks
<br>


<br>

## Criando um bucket no S3 com Cloudformation
<br>

bucket_s3.yaml

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "AWS CloudFormation Sample Template S3 bucket"
Resources: 
  NomedoRecurso:
    Type: "AWS::S3::Bucket"
    Properties:
      BucketName: Bucket-do-bootcamp
      Tags: 

```


<br>

## Introdução ao Terraform
<br>


<br>

## Criando um bucket no S3 com Terraform
<br>

<br>
