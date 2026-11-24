exercise_1_1_hint = """La fonction de correction de cet exercice attend une réponse contenant exactement les chiffres arabes "1", "2" et "3".
Vous obtiendrez souvent ce que vous voulez de Claude simplement en le lui demandant."""

exercise_1_2_hint = """La fonction de correction de cet exercice attend une réponse contenant "soo" ou "giggles" (réponse en anglais).
Il existe de nombreuses façons de résoudre cet exercice, simplement en le demandant !"""

exercise_2_1_hint ="""La fonction de correction de cet exercice attend une réponse contenant le mot "hola".
Demandez à Claude de répondre en espagnol comme vous le demanderiez à une personne. C'est aussi simple que cela !"""

exercise_2_2_hint = """La fonction de correction de cet exercice attend EXACTEMENT "Michael Jordan".
Comment le demanderiez-vous à une personne ? Répondre sans aucun autre mot ? Répondre uniquement par le nom, rien d'autre ? Il y a plusieurs façons d'aborder la réponse."""

exercise_2_3_hint = """La fonction de correction de cette cellule attend une réponse d'au moins 800 mots.
Les LLM ne savent pas encore bien compter les mots : vous devrez peut-être viser plus haut que l'objectif."""

exercise_3_1_hint = """La fonction de correction de cet exercice attend une réponse contenant les mots "incorrect" ou "not correct" (réponse en anglais).
Donnez à Claude un rôle qui pourrait l'aider à mieux résoudre les problèmes de mathématiques !"""

exercise_4_1_hint = """La fonction de correction de cet exercice attend une réponse contenant les mots "haiku" et "pig" (réponse en anglais).
N'oubliez pas d'écrire exactement "{TOPIC}" à l'endroit où le sujet doit être inséré. Si vous changez la valeur de la variable "TOPIC", Claude doit écrire un haïku sur un autre sujet."""

exercise_4_2_hint = """La fonction de correction de cet exercice attend une réponse contenant le mot "brown".
Si vous entourez "{QUESTION}" de balises XML, comment la réponse de Claude change-t-elle ?"""

exercise_4_3_hint = """La fonction de correction de cet exercice attend une réponse contenant le mot "brown".
Essayez de supprimer un mot ou un groupe de caractères à la fois, en commençant par les parties les moins compréhensibles. Procéder mot par mot vous montrera aussi jusqu'où Claude sait analyser et comprendre un texte."""

exercise_5_1_hint = """La fonction de correction de cet exercice attend une réponse contenant le mot "Warrior".
Écrivez davantage de mots à la place de Claude pour l'orienter dans la direction voulue. Par exemple, au lieu de "Stephen Curry is the best because," vous pouvez écrire "Stephen Curry is the best and here are three reasons why. 1:"."""

exercise_5_2_hint = """La fonction de correction attend une réponse de plus de 5 lignes contenant les mots "cat" et "<haiku>".
Commencez simplement. Pour l'instant, le prompt demande un seul haïku à Claude. Modifiez-le pour en demander deux (ou plus). Si vous rencontrez ensuite des problèmes de format, corrigez votre prompt une fois que Claude écrit bien plusieurs haïkus."""

exercise_5_3_hint = """La fonction de correction de cet exercice attend une réponse contenant les mots "tail", "cat" et "<haiku>".
Il est utile de découper cet exercice en plusieurs étapes.
1.	Modifiez le modèle de prompt initial pour que Claude écrive deux poèmes.
2.	Indiquez à Claude le sujet des poèmes, mais au lieu d'écrire directement les sujets (chien, chat, etc.), remplacez-les par les mots-clés "{ANIMAL1}" et "{ANIMAL2}".
3.	Exécutez le prompt et vérifiez que, dans le prompt complet, toutes les variables ont bien été remplacées. Sinon, vérifiez l'orthographe de vos balises {accolades} et qu'elles utilisent bien des accolades simples."""

exercise_6_1_hint = """La fonction de correction de cet exercice attend la lettre de la bonne catégorie, suivie de la parenthèse fermante et de la première lettre du nom anglais de la catégorie, par exemple "C) B" ou "B) B".
Procédons étape par étape :
1.	Comment Claude saura-t-il quelles catégories utiliser ? Dites-le-lui ! Incluez les quatre catégories directement dans le prompt, avec leurs lettres entre parenthèses pour faciliter la classification. N'hésitez pas à utiliser des balises XML pour organiser le prompt et montrer à Claude où commencent et finissent les catégories.
2.	Réduisez le texte superflu pour que Claude réponde immédiatement par la catégorie, et UNIQUEMENT la catégorie. Plusieurs façons de faire : parler à la place de Claude (en fournissant le début de la phrase, voire une simple parenthèse ouvrante pour qu'il comprenne que la lettre entre parenthèses doit venir en premier), ou lui dire que vous voulez la catégorie et seulement la catégorie, sans préambule.
Reportez-vous aux chapitres 2 et 5 pour revoir ces techniques.
3.	Claude peut encore se tromper de catégorie ou omettre le nom de la catégorie. Corrigez cela en lui demandant d'inclure le nom complet de la catégorie dans sa réponse.
4.	Vérifiez que {email} figure toujours quelque part dans votre modèle de prompt, pour que les e-mails à évaluer puissent y être insérés."""

exercise_6_1_solution = """
USER TURN
Please classify this email into the following categories: {email}

Do not include any extra words except the category.

<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """La fonction de correction de cet exercice attend uniquement la bonne lettre entre balises <answer>, par exemple "<answer>B</answer>". Les lettres correctes sont les mêmes que dans l'exercice précédent.
Le plus simple est parfois de donner à Claude un exemple de la sortie attendue. N'oubliez pas d'entourer votre exemple de balises <example></example> ! Et rappelez-vous que si vous pré-remplissez la réponse de Claude, ce texte ne fera pas partie de la réponse qu'il renvoie."""

exercise_7_1_hint = """Vous allez devoir écrire quelques exemples d'e-mails et les classer pour Claude (avec exactement le format voulu). Il y a plusieurs façons de faire. Voici quelques conseils.
1.	Prévoyez au moins deux exemples d'e-mails. Claude n'a pas besoin d'un exemple par catégorie, et les exemples peuvent être courts. Il est plus utile de donner des exemples pour les catégories que vous jugez les plus délicates (celles auxquelles vous avez réfléchi à la fin de l'exercice 1 du chapitre 6). Les balises XML aident à séparer les exemples du reste du prompt, sans être indispensables.
2.	Le format de vos exemples de réponse doit être exactement celui que Claude doit utiliser, pour qu'il puisse l'imiter. Ce format doit faire en sorte que la réponse de Claude se termine par la lettre de la catégorie. Là où vous placez la variable {email}, formatez-la exactement comme vos exemples d'e-mails.
3.	Gardez la liste des catégories dans le prompt, sinon Claude ne saura pas à quelles catégories se référer, ainsi que {email} comme variable de substitution."""

exercise_7_1_solution = """
USER TURN
Please classify emails into the following categories, and do not include explanations: 
<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

Here are a few examples of correct answer formatting:
<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}

ASSISTANT TURN
The correct category is:
"""
exercise_8_1_hint = """La fonction de correction de cet exercice attend une réponse contenant "I do not", "I don't" ou "Unfortunately" (réponse en anglais).
Que doit faire Claude s'il ne connaît pas la réponse ?"""

exercise_8_2_hint = """La fonction de correction de cet exercice attend une réponse contenant l'expression "49-fold".
Faites d'abord montrer à Claude son travail et son raisonnement : qu'il extraie les citations pertinentes et vérifie si elles suffisent à répondre. Reportez-vous au cours du chapitre 8 pour revoir la méthode."""

exercise_9_1_solution = """
You are a master tax acountant. Your task is to answer user questions using any provided reference documentation.

Here is the material you should use to answer the user's question:
<docs>
{TAX_CODE}
</docs>

Here is an example of how to respond:
<example>
<question>
What defines a "qualified" employee?
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>According to the provided documentation, a "qualified employee" is defined as an individual who:

1. Is not an "excluded employee" as defined in the documentation.
2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
</example>

First, gather quotes in <quotes></quotes> tags that are relevant to answering the user's question. If there are no quotes, write "no relevant quotes found".

Then insert two paragraph breaks before answering the user question within <answer></answer> tags. Only answer the user's question if you are confident that the quotes in <quotes></quotes> tags support your answer. If not, tell the user that you unfortunately do not have enough information to answer the user's question.

Here is the user question: {QUESTION}
"""

exercise_9_2_solution = """
You are Codebot, a helpful AI assistant who finds issues with code and suggests possible improvements.

Act as a Socratic tutor who helps the user learn.

You will be given some code from a user. Please do the following:
1. Identify any issues in the code. Put each issue inside separate <issues> tags.
2. Invite the user to write a revised version of the code to fix the issue.

Here's an example:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 is being squared when it's actually only the radius that should be squared>
</issue>
<response>
That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
</response>
</example>

Here is the code you are to analyze:

<code>
{CODE}
</code>

Find the relevant issues and write the Socratic tutor-style response. Do not give the user too much help! Instead, just give them guidance so they can find the correct solution themselves.

Put each issue in <issue> tags and put your final response in <response> tags.
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""Here are the functions available in JSONSchema format:

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
Retrieves a user from the database by their user ID.
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>The ID of the user to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
Retrieves a product from the database by its product ID.
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>The ID of the product to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
Adds a new user to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the user.</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>The email address of the user.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
Adds a new product to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the product.</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>The price of the product.</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""