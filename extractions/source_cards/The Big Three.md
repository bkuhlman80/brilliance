## De Raad's Explanation: Why Emotional Stability and Intellect Don't Replicate

The paper has a dedicated section titled "Emotional Stability" (p. 170\) that directly addresses this. Two reasons are given:

### 1\. Lower lexical density

Emotional Stability and Intellect typically don't emerge as the first two or three factors in any language's factor analysis — they come later, which means fewer trait terms constitute those factors. With smaller sets of items, there's less chance to capture the various facets of the construct, and less chance that those facets will align across languages.

### 2\. Clinical origins vs. everyday language

Neuroticism has its biggest constituency in clinical psychology, where its appreciation grew in specific clinical contexts. Questionnaire developers (like Costa & McCrae with the NEO) sample widely from the rich clinical vocabulary for emotional distress — anxiety, depression, hostility, self-consciousness, vulnerability, impulsiveness. But that high level of clinical specificity is not matched in the everyday lexicon of every language. The psycholexical approach captures what people actually talk about in socially relevant contexts, and the emotional-distress vocabulary varies a lot across cultures in how finely it's differentiated.

### What about Intellect/Openness?

De Raad doesn't give Intellect its own explanatory section, but there's an important footnote (footnote 2, p. 167): the German-oriented taxonomies (German, Polish, Croatian, Czech) showed relatively strong Intellect congruences in both 5- and 6-factor solutions, possibly because the German lexical tradition explicitly includes "abilities and talents" as trait descriptors. Other traditions don't, so the content that defines an Intellect factor varies radically depending on whether the taxonomy included ability-related terms.

### The broader framing

The paper's key structural insight (Table 6\) is that at the 3-factor level, the average congruences are:

* E: .78 | A: .74 (merged with H at .68) | C: .60

At the 5-factor level, S (Emotional Stability) drops to .65 and I (Intellect) to .56 — well below the .80 threshold. The paper frames this as a law of diminishing returns: adding factors beyond three buys you more coverage of the trait domain but at the cost of cross-cultural coherence.  
---

So the short version: N and O/I aren't absent from languages — they're present but inconsistently composed, because (a) they occupy a smaller lexical niche than E/A/C, (b) N's nuances are clinically enriched in some cultures but not others, and (c) Intellect's boundaries depend on whether ability terms are included in the taxonomy.

## Cutler & Condon (2022): Why Neuroticism and Openness Were Not Recovered from Language Models

Their method extracted personality structure from transformer language models (DeBERTa) using adjective similarities — no human ratings needed. The first 3 unrotated components were highly congruent with survey data (coefficients .89, .79, .79 for A, E, C). But N and O/I failed. Here's their reasoning:  
The empirical picture:

* In 5-component varimax solutions, N and I congruences with survey data were only .45 and .23  
* The 4th and 5th components explained trivially little variance (half as much as the 3rd)  
* Their content was inconsistent and hard to interpret — the 4th component mixed Neuroticism terms (introspective, emotional) with Intellect terms (philosophical, complex)  
* The 5th component was near-empty (only 7 of 435 terms loaded primarily on it)  
* No language model tested (out of 18\) recovered N or I as unique components — for all models, N and I terms were most congruent with the first component (a general evaluative/Agreeableness factor)

Their explanation:

* The unrotated structure makes it clear: the 4th and 5th components are much weaker signals than the first three. Language models, which have vastly more signal than small survey samples, make this weakness more visible, not less.  
* They argue that the "substantial increase in signal provided by the language data makes the prior weak evidence for including these traits among the most parsimonious dimensions of personality look less compelling."  
* They cite Goldberg's own admission that he "wrestled for a decade" with whether to extend Peabody's 3-factor model to Norman's 5-factor model, describing the period as "looking through a glass darkly."  
* They note the historical irony: the original NEO model (Costa & McCrae, 1978\) had only three factors (N, E, O), and the decision to add A and C was influenced by Goldberg and Digman around 1981–83.

Important caveat they include: The failure to recover N and O "does not diminish the significance of these traits" — both are reliably assessed and well-validated. The point is that they may not be the most parsimonious high-level dimensions of personality as encoded in language semantics.

**From Claude Code, analyzing papers from our repo**

Here's a synthesis of the three-factor arguments across your papers:  
Arguments for 3 (not 2 or 5\) Big Traits of Personality  
Three distinct lines of argument appear in your workspace. They converge on different trios and only partially agree.  
1\. Cross-Linguistic Replicability: E, A, C are the universal three  
De Raad et al. (2010) — XL rating  
Mega-analysis of 14 psycholexical taxonomies across 12 languages. Using Tucker's congruence (.80 threshold), only Extraversion, Agreeableness, and Conscientiousness replicate across all languages. Emotional Stability, Intellect, and Honesty-Humility fail to reach acceptable cross-linguistic congruence.  
The argument: if universality is the criterion, only three factors survive.  
2\. Semantic Structure from NLP: E, A, C (again)  
Cutler & Condon (2022) — no formal t-shirt rating in your index, but original research with novel methodology  
Used DeBERTa transformer models on personality-descriptive adjectives. The first 3 unrotated principal components from language embeddings show high congruence with survey-derived A (.79), E (.80), and C (.85). Neuroticism (.45) and Intellect (.23) are far weaker.  
The argument: the semantic structure of natural language itself encodes only three robust personality dimensions; N and O/I are secondary.

**From De Raad 2010**

the psycholexical  
approach and the Big Five model as its main spin-off have been the  
subject of serious criticisms, such as regarding its insufficiency in  
covering and representing the trait domain (e.g., Almagor et al.,  
1995; Ashton & Lee, 2001; cf. De Raad & Barelds, 2008\) and its  
lack of universality (e.g., De Raad & Peabody, 2005; De Raad,  
Perugini, et al., 1998; Peabody & De Raad, 2002). These two  
issues form opposing forces operating under the law of diminish-  
ing returns. Striving toward full coverage of the trait domain by  
increasing the number of factors increases the chance of nonrep-  
licability of such additional factors across languages.  
According to Tellegen and Waller (1987), the Big Five do not  
fully capture the language of personality because most psycholexi-  
cal studies precluded the emergence of certain dimensions—in  
particular because evaluative terms and state terms had usually  
been excluded. After applying a more liberal approach in selecting  
terms from the English lexicon, Tellegen and Waller produced a seven-factor structure on the basis of the ratings on their selected  
descriptors. That structure was supported by Almagor et al. (1995)  
and by Benet-Martı ´nez and Waller (1997), who applied the same  
liberal approach in Hebrew and Spanish, respectively (cf. Saucier,  
2003). This liberal Tellegen and Waller approach was accompa-  
nied with a dictionary sampling procedure that deviated drastically  
from the selection procedure followed in most other trait taxono-  
mies. For this reason, no effort was made to include these three  
studies in the present comparison of factor structures.  
De Raad and Szirma ´k (1994; cf. Szirma ´k & De Raad, 1994\)  
reported on a six-factor trait structure for Hungarian that included  
the Big Five and an additional factor called Integrity (with adjec-  
tives such as *veracious*, *just*, and *trustworthy* versus *hypocritical*,  
*swell-headed*, and *greedy*). De Raad and Szirma ´k tended to un-  
derstand the occurrence of this factor as an isolated event, possibly  
related to a political preoccupation in the Hungarian context. A  
factor with similar contents (called Trustworthiness) was, how-  
ever, found in Italian by Di Blas and Forzi (1999) and also  
emerged (as Truthfulness) in Korean (Hahn, Lee, & Ashton,  
1999). The repeated occurrence of this additional factor made  
Ashton, Lee, and Son (2000) propose Honesty (capturing Integrity,  
Trustworthiness, and Truthfulness) to be the sixth factor of per-  
sonality. This sixth factor was subsequently observed in French  
(Boies, Lee, Ashton, Pascal, & Nicol, 2001\) and in Dutch, Italian,  
and Polish (Ashton, Lee, Perugini, et al., 2004).  
De Raad et al.  
(1997) concluded that the first three of the Big Five factors showed  
replicability across five languages (German, Dutch, English, Hun-  
garian, Italian) and the fourth factor showed replicability in Dutch,  
Italian, and Hungarian. In De Raad, Perugini, et al. (1998), the  
American English Big Five structure was used as the target struc-  
ture with which six other Big Five structures (Dutch, German,  
Hungarian, Italian, Czech, and Polish) were compared. The general message from these studies is consistently that three, or at best  
four, of the Big Five factors are replicable across languages.  
Peabody and De Raad (2002) and De Raad and Peabody (2005)  
systematically compared the contents from five-factor and three-  
factor analyses of six European psycholexical studies (Hungarian,  
Dutch, Polish, Czech, and two Italian studies, one from Rome and  
one from Trieste). The method involved defining categories of trait  
terms according to whether they tended to stay together or to split  
apart in comparisons of five and of three factors across languages.  
The two studies generally supported the Big Three—Extraversion,  
Agreeableness, and Conscientiousness—and not the Big Five.   
In a study comparing 10 English trait factors (based on self-  
ratings from American and Australian samples on the 1,710 trait  
adjectives; see Ashton, Lee, & Goldberg, 2004\) and 10 Dutch trait  
factors (based on self-ratings on 1,203 trait adjectives), Brokken  
(1978) combined a quantitative, psychometric procedure with a  
version of the *recaptured-item technique* (RIT), which was intro-  
duced by Meehl, Lykken, Schofield, and Tellegen (1971). The RIT  
was developed to reduce the subjective element in identification of  
factors. The technique borrows its name from the success with  
which sets of items loading on certain factors but not used for the  
factor naming are identified (recaptured) on the basis of the factor  
names.1 To enable the psychometric comparison, a common base  
was constructed by translating the Dutch adjectives into English.  
The English and Dutch matrices of loadings on 10 factors for a  
common set of 300 trait adjectives were used for the comparison.  
Congruence coefficients calculated after rotating the English struc-  
ture to the Dutch structure suggested two to four similar factors  
(with coefficients of 0.93, 0.88, 0.79, and 0.78). In addition, sets of  
trait adjectives representing the 10 Dutch and the 10 English  
factors were administered to subjects who were asked to match the  
10 Dutch sets to the 10 English sets. This judging procedure  
resulted in an almost perfect match of the first seven factors. The  
discrepancy between the two to four replicable factors according to  
psychometric criteria and the seven replicable factors according to  
intersubjective criteria perfectly exemplifies the different attitudes  
toward factor recurrence across languages.  
The emergence of the Big Five model has been accompanied by  
questions concerning its universality and its coverage of the trait  
domain. Although the model is widely accepted and applied, its  
cross-cultural replicability has not matched its cross-cultural pop-  
ularity. From comparisons among different five-factor structures  
developed within the psycholexical tradition, no more than three or  
four of the Big Five factors have shown replicability across languages. Furthermore, strong claims have recently been made for a  
six-factor model that includes versions of the Big Five and an  
additional factor, called Honesty-Humility. Given the findings  
with respect to the Big Five factors, one wonders how factors  
beyond the Big Five (i.e., a six-factor structure) could claim a  
cross-cultural position at all. Indeed, the present findings did not  
support cross-cultural replicability of a six-factor structure. Rather,  
the findings support that, on average, only the first three factors of  
the Big Five or of the six-factor model are robustly replicable, thus  
suggesting substantial “universality” of a Big Three. These results  
are consistent with our expectation regarding the greater cross-  
cultural replicability of the three-factor structure.  
The results from the initial factor identification procedure based  
on the six-factor marker scales indicate that factor solutions with  
one, two, or three factors are rather consistently identified as ACH  
related (one factor), ESI and ACH related (two factors), and E,  
AH, and C related (three factors), respectively. With four factors,  
the fourth factor is ambiguously and less substantially S or I  
related; with five factors kernel characteristics of the Big Five are  
identified consistently, but relatively less substantially for the  
I-related factor. Finally, with six factors, inconsistencies can be  
observed, especially for the sixth factor. In conclusion, broad  
versions of the Big Three with kernel characteristics of E, A, and  
C are most replicable.  
The results from the factor comparisons using congruence co-  
efficients point in the same direction. Generally, structures with no  
more than three factors are replicable across languages; for struc-  
tures with more than three factors, on average only the first three  
reach an acceptable level of cross-cultural validity.  
**Relationship to Previous Findings**  
The history of psycholexical studies has demonstrated interest in  
the recurrence of trait structures with one to seven factors. We  
briefly review the relevant literature in relation to the present  
findings. Cross-language seven-factor structures refer to the dis-  
sonant Tellegen and Waller (1987) design applied in English and  
later in Spanish (Benet-Martı ´nez & Waller, 1997\) and Hebrew  
(Almagor et al., 1995). However, the Spanish (Benet-Martı ´nez &  
Waller, 1997\) and Hebrew (Almagor et al., 1995\) lexical studies  
followed a dictionary sampling procedure, which reduced the  
representativeness of the trait terms. Moreover, these studies explicitly included highly evaluative and state descriptors. Therefore,  
seven-factor structures are not further discussed here.  
**One-factor model.** Interest in the relevance of a single gen-  
eral factor of personality goes back to Webb (1915), who searched  
for a broad factor *w* of personality, comparable to a general factor  
of intelligence. Such a general factor, called the *p* factor by  
Hofstee (2001), results from taking the first principal component  
of a broad set of personality trait variables. The content is deter-  
mined by the fact that the large majority of personality factors,  
scored in a socially desirable direction, intercorrelate positively.  
Some might want to call this factor Social Desirability, but there is  
more to this factor than being an artifact. According to Hofstee, the  
*p* factor combines stylistic intellect and other personality traits,  
enabling a person to react adequately to situations. Musek (2007)  
studied the Big One using Big Five scales and items, and he related  
that general factor to all of the Big Five factors. Rushton, Bons,  
and Hur (2008) reported similar findings using different sets of  
personality scales. In a comprehensive, large-scale psycholexical  
study in Dutch, De Raad and Barelds (2008) labeled the first factor  
in a hierarchy of factors Virtue, of which the content was mainly  
described in terms of Agreeableness-related items. The present  
findings (see Table 5), based on the study of 14 taxonomies,  
suggest that the kernel of the first unrotated factor is mainly  
characterized by Agreeableness, Conscientiousness, and, to a  
lesser extent, by Emotional Stability. There seems to be an overall  
robust emergence of a single factor. Further research should ad-  
dress the specific contents of that factor in detail and give a precise  
account of the extent to which such a first factor reflects trait  
content, judgment style, and choice of method.  
**Two-factor model.** Digman (1997) factored Big Five corre-  
lations from 14 studies and distinguished two higher order factors  
called Alpha and Beta. Alpha combined the Big Five factors  
Agreeableness, Conscientiousness, and Emotional Stability, and  
Beta combined Extraversion and Intellect. The two higher order  
factors were related to a two-dimensional system—*agency* and  
*communion*—previously described by Bakan (1966) and Wiggins  
(1991) to summarize the domain of interpersonal behavior. Sup-  
port for this two-dimensional system was reported in both Musek  
(2007) and Rushton et al. (2008). Typical of the Agency/Beta  
dimension is the emphasis on individual striving and personal  
achievement; typical of the Communion/Alpha dimension is the emphasis on social interest and on being part of a larger whole.  
The two-factor solution in De Raad and Barelds (2008) does  
support such a general distinction. The present findings combine  
the Big Five factors somewhat differently than was done in Dig-  
man (1997), Musek (2007), and Rushton et al. (2008), with Emo-  
tional Stability clustering together with Extraversion and Intellect  
(see Table 5).  
**Three-factor model.** With three factors, a rather coherent and  
cross-culturally replicated system emerged with Extraversion,  
Agreeableness, and Conscientiousness as the typical, distinguish-  
ing features. The emergence of this three-factor system agrees with  
the recent lexical history (cf. Saucier et al., 2000). Peabody and  
Goldberg (1989; cf. Saucier, 1998\) concluded that the most robust  
version of the American English Big Five could consist of three  
large factors (Extraversion, Agreeableness, and Conscientious-  
ness) and two smaller, less replicable factors. For both German  
(Ostendorf, 1990\) and Croatian (Mlac ˇic ´ & Ostendorf, 2005), three-  
factor solutions were reported to be more replicable than five-  
factor solutions. In the Italian Triestean project (Di Blas & Forzi,  
1998), the Big Three turned out to be identifiable in two different  
samples. This Big Three structure was replicated in still another  
sample (Di Blas & Forzi, 1999). A Turkish lexical study (Somer &  
Goldberg, 1999\) produced a clean Big Five solution; in addition,  
for both self-ratings and peer ratings, a three-factor solution pro-  
duced broad versions of the Big Three. On the Filipino study  
(Church, Katigbak, & Reyes, 1998), Saucier et al. (2000) sug-  
gested that a three-factor solution did not include broad versions of  
the Big Three but that instead “Agreeableness and Conscientious-  
ness content remained intertwined until a lower level in the hier-  
archical structure” (p. 20). That observation was not definitively  
confirmed in the present study, where a general characterization in  
terms of the Big Three labels received support in the marker scale  
analysis (see Table 5).  
**Four-factor model.** Because lexically based structures with  
four factors have not been published very frequently, such a  
possibility is also not discussed in this section.  
**Five-factor model.** With five factors, the cross-cultural find-  
ings are very consistent. Studies that use interpretive evaluations of  
factors tend to report in an affirmative sense on the Big Five (cf.  
De Raad & Peabody, 2005). Nonetheless, studies in which several  
taxonomies were systematically compared confirmed no more than  
three or four of the Big Five factors. Such was the case in Hofstee  
et al. (1997), where in a comparison of three Germanic lexical  
studies the congruencies between corresponding factors clearly  
dropped below the level of similarity maintained in the present  
study after three factors. A similar pattern of average congruencies  
was reported in a comparison of five lexical studies (De Raad et  
al., 1997\) and in a comparison of seven lexical studies with  
American English as the target (De Raad, Perugini, et al., 1998). In  
a systematic comparison of the item contents used in six lexical  
studies, Peabody and De Raad (2002) and De Raad and Peabody  
(2005) showed that a coherent classification of lexical items was  
possible with three factors, but not with five. The average results  
of five-factor comparisons from the present 14 taxonomies con-  
firm these earlier findings.  
**Six-factor model.** Also with six factors, the first three factors  
generally recur across languages, with congruencies clearly drop-  
ping below an acceptable threshold after three factors. In their  
review of eight six-factor structures, Ashton, Lee, Perugini, et al. (2004) stated that “a similar six-factor solution has emerged from  
self-ratings on the familiar personality-descriptive adjectives”  
(p. 364). Why could Ashton, Lee, Perugini, et al. arrive at such a  
conclusion, when the present study could not? If we restrict our-  
selves to the eight structures that were used by Ashton, Lee,  
Perugini, et al. to reach their conclusion, our results for those eight  
structures do not warrant a conclusion different from the one we  
drew on the basis of the 14 structures. Also, if the restriction is  
made to self-ratings, no different conclusion is reached. We be-  
lieve that the discrepancy between the findings is found in a  
combination of choice of structures to compare, rotations made of  
some factors in some structures toward a certain position of the  
factors, and evaluations of the factors at face value (on the basis of  
interpretations of factors only). As regards the latter, De Raad and  
Peabody (2005) have warned against the dangers of circular rea-  
soning in the identification of factors. Just as it has happened with  
respect to the identification of Big Five factors in new data sets,  
assuming the generality of the six-factor structure (including the  
Honesty-Humility factor), which generality still needs to be dem-  
onstrated, may easily lead to a premature factor identification.  
**Emotional Stability**  
The finding that Emotional Stability (or Neuroticism) exhibits  
weaker replication in lexical studies contrasts with its historical  
prominence. From early personality psychology on, virtually all  
trait models and personality questionnaires included Neuroticism.  
Therefore, the failure of this dimension in particular, to replicate  
well across cultures warrants comment. One reason why Emo-  
tional Stability does not replicate well may be its lesser represen-  
tation in most natural languages. As is also true for Intellect,  
Emotional Stability most typically does not belong to the first two  
or three factors extracted in the factor analyses, which is an  
indication of a smaller density of terms constituting those factors.  
In case of smaller sets of items, there is clearly less chance to  
capture the various possible facets of the construct.  
The psycholexical approach is designed to elicit those attributes  
that are most talked about in a variety of socially relevant contexts.  
Neuroticism or Emotional Stability has a large constituency in  
clinical psychology, where its appreciation has grown in specific  
clinical contexts. To capture the many nuances of emotional ex-  
periences, questionnaire developers may sample widely from the  
rich variety of specific variables from the clinical field. Such a  
high level of specificity is possibly not matched in the context of  
every language.  
**Inclusion of Structures for the Comparison**  
The choice of structures for the comparison may make a differ-  
ence. English, Filipino, and Czech were not included in the Ash-  
ton, Lee, Perugini, et al. (2004) study, and those three structures  
had a relatively negative effect on the general level of congruence  
coefficients found for the Honesty-Humility factor in the present  
comparisons. Greek, another structure not included in the Ashton,  
Lee, Perugini, et al. (2004) study, did not differ much from the  
general averages, and only one new structure, Croatian, contrib-  
uted relatively positively toward the general level of congruence  
for Honesty-Humility. With the fewer structures studied by Ash-  
ton, Lee, Perugini, et al., there may have been a tendency to interpret deviating results with more leniency. For English, addi-  
tional efforts were made to find an articulate six-factor structure in  
new data sets, but with little success (Ashton, Lee, & Goldberg,  
2004; Lee & Ashton, 2008).  
**Rotations of Factors**  
Ashton, Lee, Perugini, et al. (2004) rerotated the second- and  
sixth-largest factors of the Italian (Trieste) structure, and the third  
and sixth factors of the Korean structure, to arrive at a clearer  
version of the Intellect-Imagination factors in both studies. Such  
rerotations for the purposes of getting a clearer structure are just  
fine, the condition being that one could expect a structure to appear  
in the various languages on the basis of an established model, but  
that is exactly what has to be shown first. If such rotations had  
been applied in the present study, in particular on Factors II  
(Agreeableness) and VI (Honesty-Humility) in the different factor  
analyses before the structures were submitted to the present pro-  
cedures, the outcomes would have been different. The 14 struc-  
tures in the present study are all taken in their “natural” arrange-  
ment, which from an exploratory viewpoint best reflects the gist of  
the psycholexical approach. No effort was made to arrive at a  
better alignment to the contents of preconceived five- or six-factor  
models.  
There is no doubt that Honesty-Humility should be considered  
as a cluster of traits with a certain level of coherence. The issue  
here is the interconnectedness of the factors Agreeableness (II)  
and Honesty-Humility (VI). Assuming a broad definition of  
Honesty-Humility as was done in this study, including references  
to honesty–sincerity and helpfulness–altruism (see Using factor  
markers), it is questionable whether Honesty-Humility can stand  
on its own feet as a separate factor. If so, this could probably be the  
case only if the traditional Agreeableness conceptualization is  
disposed of some hitherto characteristic facets. In the case of a  
narrow definition of Honesty-Humility (without the helpfulness–  
altruism reference), it would function well to occupy a distinct  
niche in the Big Five system. In the American English and Dutch  
Big Five circumplex configurations, for example, the kernel of  
such a cluster is represented in the II III and III II facets  
(and their counterparts II III and III II ; Hofstee, De Raad, &  
Goldberg, 1992; De Raad et al., 1992). Such a narrow Honesty-  
Humility cluster is almost invariably part of a broad Big Five  
Agreeableness factor.  
