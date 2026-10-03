# Blind review report

980 items, 980 verdict rows matched, 0 stray rows.

An item is **verified** only if it was judged (not abstained), the label agrees, the
reviewer confirms the stated language, reads it with high or medium
confidence, is not unsure of the label, does not find the policy ambiguous on it,
and does not find it garbled. Everything else carries the first reason that
applies, in the column order below. Only verified items enter the analysis.

**Verified: 772 of 980.**

## Per language

| lang | items | verified | missing | invalid | abstained | disputed | wrong_language | language_unknown | policy_ambiguous | label_unsure | reading_low | garbled | category differs | reading medium |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| en | 55 | 47 | 0 | 0 | 0 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 4 | 0 |
| de | 55 | 45 | 0 | 0 | 0 | 8 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 |
| fr | 55 | 43 | 0 | 0 | 2 | 6 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 2 |
| es | 55 | 43 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| it | 55 | 49 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 4 |
| pt | 40 | 26 | 0 | 0 | 2 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| nl | 40 | 26 | 0 | 0 | 0 | 10 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 2 |
| pl | 40 | 28 | 0 | 0 | 0 | 8 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| cs | 40 | 36 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 8 |
| hu | 40 | 32 | 0 | 0 | 0 | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 32 |
| ro | 20 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 |
| sv | 40 | 34 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| fi | 40 | 28 | 0 | 0 | 0 | 6 | 0 | 0 | 6 | 0 | 0 | 0 | 4 | 28 |
| tr | 40 | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| vi | 37 | 29 | 0 | 0 | 0 | 4 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 29 |
| id | 17 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| el | 20 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 |
| ru | 40 | 34 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| uk | 20 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| ar | 40 | 25 | 0 | 0 | 3 | 10 | 0 | 0 | 2 | 0 | 0 | 0 | 4 | 25 |
| hi | 40 | 28 | 0 | 0 | 0 | 2 | 0 | 0 | 8 | 0 | 2 | 0 | 0 | 28 |
| th | 40 | 24 | 0 | 0 | 0 | 8 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 24 |
| ja | 37 | 25 | 0 | 0 | 0 | 10 | 0 | 0 | 2 | 0 | 0 | 0 | 6 | 2 |
| ko | 37 | 24 | 0 | 0 | 2 | 6 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 24 |
| zh | 37 | 29 | 0 | 0 | 0 | 4 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| all | 980 | 772 | 0 | 0 | 9 | 132 | 0 | 0 | 59 | 0 | 8 | 0 | | |

`category differs` and `reading medium` are counted among verified items and do not block verification.

## Items to look at

### es-s-fo-04 - verified (flag / profanity / obfuscated)

- text: `Conchetumare Clips Chile`
- intended: Chile: decoded 'concha de tu madre' (your mother's cunt); technique: respelled (phonetic run-together Chilean spelling 'conchetumare')
- reviewer gloss: Your mother's cunt clips, Chile
- reviewer: label flag, category profanity, decoded Concha de tu madre, reading high, label confidence high
- issue: Chilean fused profanity.

### en-x-fp-01 - disputed (flag / profanity / lexicon_plain)

- text: `Zoophilia TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Sexual attraction to animals TV
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic naming of a sexual condition is not promotion or an explicit act; the policy leaves this standalone name unresolved.

### en-x-fo-01 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Z00ph1l14 TV`
- intended: same term as en-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Sexual attraction to animals TV
- reviewer: label clean, category none, decoded Zoophilia, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: A non-graphic name of a paraphilia does not describe or promote an act; the policy leaves standalone sexual-topic names unresolved.

### en-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `Panty 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Panty 24
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### en-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Раntу 24`
- intended: same term as en-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Panty 24
- reviewer: label clean, category none, decoded Panty, reading high, label confidence high
- label: intended flag, reviewer clean

### en-x-fp-06 - disputed (flag / profanity / lexicon_plain)

- text: `Clitoris TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Clitoris TV
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: The policy does not resolve bare anatomical public names without sexual or medical context.

### en-x-fo-06 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Cl1t0r15 TV`
- intended: same term as en-x-fp-06, disguised by code; technique: leet
- reviewer gloss: Clitoris TV
- reviewer: label clean, category none, decoded Clitoris, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: The policy does not specify treatment of a bare anatomical public name outside medical context.

### en-x-fp-07 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Bitch HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bitch HD
- reviewer: label flag, category profanity, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Can mean a female dog or be profanity; the bare name gives no context to settle policy application.

### en-x-fo-07 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `B.i.t.c.h HD`
- intended: same term as en-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Bitch HD
- reviewer: label flag, category profanity, decoded Bitch, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Can be profanity or an ordinary female-dog noun; the policy does not resolve the isolated name's use.

### de-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `Kimme HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Rear sight / butt crack HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary firearm-part meaning competes with a coarse anatomical sense; acceptability of the contextless name is not settled by the policy.

### de-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `K.i.m.m.e HD`
- intended: same term as de-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Rear sight / butt crack HD
- reviewer: label clean, category none, decoded Kimme, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: An ordinary technical noun also has a coarse anatomical meaning; the policy leaves this standalone use unresolved.

### de-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `Möpse 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Pugs / tits 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Normal word for pugs also has a slang breast meaning; the policy gives no contextless-name boundary.

### de-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Möрsе 24`
- intended: same term as de-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Pugs / tits 24
- reviewer: label clean, category none, decoded Möpse, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: A normal dog word also means breasts in slang; the policy does not determine this contextless use.

### de-x-fp-05 - disputed (flag / profanity / lexicon_plain)

- text: `Nippel 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Nipple / projecting knob 7
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic anatomy or a technical knob; the policy leaves isolated names of this kind unresolved.

### de-x-fo-05 - disputed (flag / profanity / lexicon_obfuscated)

- text: `N*ppel 7`
- intended: same term as de-x-fp-05, disguised by code; technique: masked
- reviewer gloss: Nipple / projecting knob 7
- reviewer: label clean, category none, decoded Nippel, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Anatomical and technical senses are possible; the policy does not define when a bare anatomical name is sexual content.

### de-x-fp-09 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Muschi FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Pussy / kitty FM
- reviewer: label flag, category profanity, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Both a vulgar genital term and an affectionate word for a cat; the policy does not settle the contextless public name.

### de-x-fo-09 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Muuuschi FM`
- intended: same term as de-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Pussy / kitty FM
- reviewer: label flag, category profanity, decoded Muschi, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Vulgar genital sense and innocent cat sense coexist; the isolated name gives no context to resolve the policy application.

### de-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `Schiesser 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Schiesser 7
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: Schiesser is a surname and brand; it is not Scheißer, the vulgar word.

### de-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Sch*esser 7`
- intended: same term as de-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Sch*esser 7, possibly the name Schiesser
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- issue: The mask could also yield the vulgar Scheisser; I cannot uniquely decode it and retain the readable surname interpretation.

### fr-x-fp-01 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Baiser TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To fuck / a kiss TV
- reviewer: label flag, category sexual, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Verb and innocent noun readings coexist; the policy leaves the isolated name unresolved.

### fr-x-fo-01 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `B4153r TV`
- intended: same term as fr-x-fp-01, disguised by code; technique: leet
- reviewer gloss: To fuck / a kiss TV
- reviewer: label flag, category sexual, decoded Baiser, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Verb means to fuck; noun means a kiss. The policy cannot resolve the intended reading of the bare public name.

### fr-x-fp-02 - verified (flag / profanity / lexicon_plain)

- text: `Brackmard HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Dick HD
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Informal spelling related to braquemart; vulgar penis term.

### fr-x-fo-02 - verified (flag / profanity / lexicon_obfuscated)

- text: `B.r.a.c.k.m.a.r.d HD`
- intended: same term as fr-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Dick HD
- reviewer: label flag, category profanity, decoded Brackmard, reading medium, label confidence high
- issue: Informal vulgar penis term, related to braquemart.

### fr-x-fp-03 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Chatte 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Pussy / female cat 24
- reviewer: label flag, category profanity, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: The vulgar genital meaning and innocent cat meaning are both possible; the policy leaves this contextless name unresolved.

### fr-x-fo-03 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Сhаttе 24`
- intended: same term as fr-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Pussy / female cat 24
- reviewer: label flag, category profanity, decoded Chatte, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Genital and innocent feline meanings coexist; the contextless public name is unresolved by the policy.

### fr-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `Déconne HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Joking / messing around HD
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: Common colloquial verb, with no offensive target or explicit content in this name.

### fr-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `D.é.c.o.n.n.e HD`
- intended: same term as fr-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Joking / messing around HD
- reviewer: label clean, category none, decoded Déconne, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: Common colloquial verb can be non-offensive; no target or explicit content here.

### fr-x-fp-08 - disputed (flag / profanity / lexicon_plain)

- text: `Bitte 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bollard 24
- reviewer: label clean, category none, decoded None, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: Correct French nautical noun; bite, with one t, is the usual vulgar penis term. This could be a nonstandard spelling, but that is uncertain.

### fr-x-fo-08 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Bіttе 24`
- intended: same term as fr-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Bollard 24
- reviewer: label clean, category none, decoded Bitte, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: French bitte is a nautical bollard; the vulgar penis word is normally bite. A nonstandard vulgar spelling is possible but not established here.

### fr-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `Caca 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Poop 7
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Childish bodily word rather than a strong swear; the policy does not define whether such a standalone name falls under obscenity or mild slang.

### fr-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `C*ca 7`
- intended: same term as fr-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Poop 7
- reviewer: label clean, category none, decoded Caca, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Childish excrement word; the policy leaves its boundary with permitted mild slang or obscenity open.

### es-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `Martillo HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Hammer HD
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### es-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `M.a.r.t.i.l.l.o HD`
- intended: same term as es-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Hammer HD
- reviewer: label clean, category none, decoded Martillo, reading high, label confidence high
- label: intended flag, reviewer clean

### es-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `Imbécil FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Imbecile FM
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Targetless insulting word; the policy gives no boundary for a rude display name.

### es-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Imbééécil FM`
- intended: same term as es-x-fp-04, disguised by code; technique: stretched
- reviewer gloss: Imbecile FM
- reviewer: label clean, category none, decoded Imbécil, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Targetless insulting word; the policy leaves the boundary between rudeness and harassment open.

### es-x-fp-05 - disputed (flag / profanity / lexicon_plain)

- text: `Esperma 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Sperm 7
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic biological term; the policy does not specify whether an isolated public name without educational context is acceptable.

### es-x-fo-05 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Esp*rma 7`
- intended: same term as es-x-fp-05, disguised by code; technique: masked
- reviewer gloss: Sperm 7
- reviewer: label clean, category none, decoded Esperma, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Biological noun without graphic sexual content; acceptability as a public name outside education is underspecified.

### es-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `Idiota HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Idiot HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: The policy does not specify whether a targetless insult used as a display name counts as harassment.

### es-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `I.d.i.o.t.a HD`
- intended: same term as es-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Idiot HD
- reviewer: label clean, category none, decoded Idiota, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: An isolated insult with no target; the policy does not say when such a public name constitutes harassment rather than mild rudeness.

### es-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `Asesinato FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Murder FM
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Names violence without describing, endorsing or glorifying it; the policy leaves treatment of such contextless names unclear.

### es-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Aseeesinato FM`
- intended: same term as es-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Murder FM
- reviewer: label clean, category none, decoded Asesinato, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: The word names violence without advocating it; the policy leaves contextless violent-topic names unresolved.

### es-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `Macizorra 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Very hot woman 7
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Coarse objectifying slang without explicit sex or a personal target; the policy does not resolve the boundary.

### es-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `M*cizorra 7`
- intended: same term as es-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Very hot woman 7
- reviewer: label clean, category none, decoded Macizorra, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Coarse objectifying slang, but no explicit sex or personal target; the policy leaves this boundary open.

### it-x-fp-02 - verified (flag / profanity / lexicon_plain)

- text: `Bagassa HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Whore HD
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Regional vulgar term for a prostitute.

### it-x-fo-02 - verified (flag / profanity / lexicon_obfuscated)

- text: `B.a.g.a.s.s.a HD`
- intended: same term as it-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Whore HD
- reviewer: label flag, category profanity, decoded Bagassa, reading medium, label confidence high
- issue: Regional vulgar term for a prostitute.

### it-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `Slinguare FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To French-kiss FM
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic intimate act; the policy does not specify whether this standalone name is sexually explicit enough to flag.

### it-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Sliiinguare FM`
- intended: same term as it-x-fp-04, disguised by code; technique: stretched
- reviewer gloss: To French-kiss FM
- reviewer: label clean, category none, decoded Slinguare, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic kissing term; the policy leaves the boundary with sexually explicit names open.

### it-x-fp-06 - verified (flag / profanity / lexicon_plain)

- text: `Busone TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Faggot TV
- reviewer: label flag, category hate, decoded None, reading medium, label confidence high
- issue: Regional derogatory term for a gay man.

### it-x-fo-06 - verified (flag / profanity / lexicon_obfuscated)

- text: `Bu50n3 TV`
- intended: same term as it-x-fp-06, disguised by code; technique: leet
- reviewer gloss: Faggot TV
- reviewer: label flag, category hate, decoded Busone, reading medium, label confidence high
- issue: Regional derogatory term for a gay man.

### it-x-fp-08 - reading_low (flag / profanity / lexicon_plain)

- text: `Fracicone 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Faggot / rotten fellow 24
- reviewer: label flag, category hate, decoded None, reading low, label confidence high
- reviewer reads this item poorly
- issue: Regional derogatory homosexual use is recognizable, but my command of this dialect term's precise range is limited.

### it-x-fo-08 - reading_low (flag / profanity / lexicon_obfuscated)

- text: `Frасісоnе 24`
- intended: same term as it-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Faggot / rotten fellow 24
- reviewer: label flag, category hate, decoded Fracicone, reading low, label confidence high
- reviewer reads this item poorly
- issue: I recognize a regional derogatory homosexual sense, but am less certain of its range than of ordinary Italian profanity.

### it-x-fp-10 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Sega 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: A wank / saw 7
- reviewer: label flag, category sexual, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Ordinary tool noun and vulgar masturbation sense coexist; policy application cannot be settled from the bare name.

### it-x-fo-10 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `S*ga 7`
- intended: same term as it-x-fp-10, disguised by code; technique: masked
- reviewer gloss: A wank / saw 7
- reviewer: label flag, category sexual, decoded Sega, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Tool and vulgar masturbation senses coexist; the policy does not resolve the isolated name.

### pt-x-fp-01 - disputed (flag / profanity / lexicon_plain)

- text: `Aborto TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Abortion TV
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### pt-x-fo-01 - disputed (flag / profanity / lexicon_obfuscated)

- text: `4b0rt0 TV`
- intended: same term as pt-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Abortion TV
- reviewer: label clean, category none, decoded Aborto, reading high, label confidence high
- label: intended flag, reviewer clean

### pt-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `Mama HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Breast / suck / suckle HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary anatomical or nursing word also permits a sexual imperative reading; the policy does not resolve the contextless name.

### pt-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `M.a.m.a HD`
- intended: same term as pt-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Breast / suck / suckle HD
- reviewer: label clean, category none, decoded Mama, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Nursing/anatomy sense or sexual imperative reading; policy application cannot be settled from the bare name.

### pt-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `Aranha 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Spider 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary noun with a possible genital-slang sense; the policy does not resolve a contextless public name.

### pt-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Аrаnhа 24`
- intended: same term as pt-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Spider 24
- reviewer: label clean, category none, decoded Aranha, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary animal noun can also be genital slang; the policy does not resolve which sense a contextless name invokes.

### pt-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `Peidar HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To fart HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-sexual bodily slang; the policy gives no clear boundary for obscenity versus mild slang in this name.

### pt-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `P.e.i.d.a.r HD`
- intended: same term as pt-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: To fart HD
- reviewer: label clean, category none, decoded Peidar, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-sexual bodily slang; the policy leaves its boundary with obscenity unresolved for an isolated name.

### pt-x-fp-08 - disputed (flag / profanity / lexicon_plain)

- text: `Burro 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Donkey / stupid 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Animal noun or targetless insult; the policy does not resolve the rudeness/harassment boundary for this name.

### pt-x-fo-08 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Burrо 24`
- intended: same term as pt-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Donkey / stupid 24
- reviewer: label clean, category none, decoded Burro, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Animal word or targetless insult; the policy leaves this name's rudeness/harassment boundary open.

### pt-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `Inferno FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Hell FM
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### pt-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Infeeerno FM`
- intended: same term as pt-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Hell FM
- reviewer: label clean, category none, decoded Inferno, reading high, label confidence high
- label: intended flag, reviewer clean

### nl-x-fp-01 - disputed (flag / profanity / lexicon_plain)

- text: `Remsporen TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Skid marks TV
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### nl-x-fo-01 - disputed (flag / profanity / lexicon_obfuscated)

- text: `R3m5p0r3n TV`
- intended: same term as nl-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Skid marks TV
- reviewer: label clean, category none, decoded Remsporen, reading high, label confidence high
- label: intended flag, reviewer clean

### nl-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `Stootje HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Little bump / attractive woman HD
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: Ordinary diminutive or mild appreciative slang, with no explicit sex or abusive target.

### nl-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `S.t.o.o.t.j.e HD`
- intended: same term as nl-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Little bump / attractive woman HD
- reviewer: label clean, category none, decoded Stootje, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: Ordinary diminutive or mild appreciative slang, with no explicit sex or abusive target.

### nl-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `Kont 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Butt / backside 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Mild coarse anatomy word, not explicit sex; the policy does not define when such a bare public name is obscene.

### nl-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Kоnt 24`
- intended: same term as nl-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Butt / backside 24
- reviewer: label clean, category none, decoded Kont, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Mild coarse anatomical noun without explicit sex; policy leaves contextless naming unresolved.

### nl-x-fp-05 - verified (flag / profanity / lexicon_plain)

- text: `Afberen 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To jerk off 7
- reviewer: label flag, category sexual, decoded None, reading medium, label confidence high
- issue: Regional vulgar masturbation verb.

### nl-x-fo-05 - verified (flag / profanity / lexicon_obfuscated)

- text: `Afb*ren 7`
- intended: same term as nl-x-fp-05, disguised by code; technique: masked
- reviewer gloss: To jerk off 7
- reviewer: label flag, category sexual, decoded Afberen, reading medium, label confidence high
- issue: Regional vulgar masturbation verb.

### nl-x-fp-07 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Oprotten HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Piss off / get lost HD
- reviewer: label flag, category profanity, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse imperative without a named target; policy leaves the boundary between rudeness and profanity open.

### nl-x-fo-07 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `O.p.r.o.t.t.e.n HD`
- intended: same term as nl-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Piss off / get lost HD
- reviewer: label flag, category profanity, decoded Oprotten, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse imperative with no identified target; policy leaves the rudeness/profanity boundary open.

### nl-x-fp-08 - disputed (flag / profanity / lexicon_plain)

- text: `Zuiplap 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Drunkard 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Targetless insulting description; policy does not define the line between a rude display name and harassment.

### nl-x-fo-08 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Zuірlар 24`
- intended: same term as nl-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Drunkard 24
- reviewer: label clean, category none, decoded Zuiplap, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Insulting description without a target; the policy does not define when a rude public name becomes harassment.

### nl-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `Poep FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Poop / backside FM
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### nl-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Poooep FM`
- intended: same term as nl-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Poop / backside FM
- reviewer: label clean, category none, decoded Poep, reading high, label confidence high
- label: intended flag, reviewer clean

### nl-x-fp-10 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Flikker 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Faggot / flicker 7
- reviewer: label flag, category hate, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Common slur and non-abusive noun/verb readings coexist; the policy does not resolve the standalone name.

### nl-x-fo-10 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Fl*kker 7`
- intended: same term as nl-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Faggot / flicker 7
- reviewer: label flag, category hate, decoded Flikker, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Slur and non-abusive readings coexist; the isolated name does not settle the policy application.

### pl-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `Pierdzieć HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To fart HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Bodily slang without an abusive target; the policy leaves the obscenity/mild-slang boundary open.

### pl-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `P.i.e.r.d.z.i.e.ć HD`
- intended: same term as pl-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: To fart HD
- reviewer: label clean, category none, decoded Pierdzieć, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-sexual bodily slang; the policy does not clearly settle whether this standalone name is obscene or mild.

### pl-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `Jajco 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Egg / ball 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Colloquial egg word can also refer to a testicle; the policy gives no boundary for this mild anatomical name.

### pl-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Jаjсо 24`
- intended: same term as pl-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Egg / ball 24
- reviewer: label clean, category none, decoded Jajco, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Colloquial egg or testicle; the policy leaves the bare name's mild-slang boundary unresolved.

### pl-x-fp-04 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Suka FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bitch / female dog FM
- reviewer: label flag, category profanity, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Ordinary animal and abusive meanings coexist; the contextless public name is unresolved.

### pl-x-fo-04 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Suuuka FM`
- intended: same term as pl-x-fp-04, disguised by code; technique: stretched
- reviewer gloss: Bitch / female dog FM
- reviewer: label flag, category profanity, decoded Suka, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Literal dog noun and insult coexist; there is no context to settle policy application.

### pl-x-fp-05 - disputed (flag / profanity / lexicon_plain)

- text: `Rzygać 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To puke 7
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Coarse non-sexual bodily verb; the policy does not clearly settle the acceptability of the standalone name.

### pl-x-fo-05 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Rz*gać 7`
- intended: same term as pl-x-fp-05, disguised by code; technique: masked
- reviewer gloss: To puke 7
- reviewer: label clean, category none, decoded Rzygać, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Coarse bodily verb without explicit sex or a target; policy does not resolve the slang/obscenity boundary of a bare name.

### pl-x-fp-06 - disputed (flag / profanity / lexicon_plain)

- text: `Dmuchać TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To blow / to fuck TV
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary blowing verb also has sexual slang use; the policy does not resolve the contextless name.

### pl-x-fo-06 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Dmuch4ć TV`
- intended: same term as pl-x-fp-06, disguised by code; technique: leet
- reviewer gloss: To blow / to fuck TV
- reviewer: label clean, category none, decoded Dmuchać, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary blowing verb and sexual slang coexist; the isolated name does not settle application of the policy.

### pl-x-fp-09 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Sraczka FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: The shits / diarrhea FM
- reviewer: label flag, category profanity, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Crude diarrhea term; the policy leaves its boundary with permitted mild bodily slang open.

### pl-x-fo-09 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Sraaaczka FM`
- intended: same term as pl-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: The shits / diarrhea FM
- reviewer: label flag, category profanity, decoded Sraczka, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse bodily term rather than a strong curse; the policy leaves its obscenity/mild-slang boundary open.

### cs-x-fp-04 - verified (flag / profanity / lexicon_plain)

- text: `Mrdník FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Fucking mess / fuck den FM
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Vulgar word; exact sense depends on context.

### cs-x-fo-04 - verified (flag / profanity / lexicon_obfuscated)

- text: `Mrdnííík FM`
- intended: same term as cs-x-fp-04, disguised by code; technique: stretched
- reviewer gloss: Fucking mess / fuck den FM
- reviewer: label flag, category profanity, decoded Mrdník, reading medium, label confidence high
- issue: Vulgar word with context-dependent senses.

### cs-x-fp-05 - disputed (flag / profanity / lexicon_plain)

- text: `Držka 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Mug / muzzle 7
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Coarse word for a mouth or face, also an animal's muzzle; the policy does not resolve a rude standalone word without a target.

### cs-x-fo-05 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Držk* 7`
- intended: same term as cs-x-fp-05, disguised by code; technique: masked
- reviewer gloss: Mug / muzzle 7
- reviewer: label clean, category none, decoded Držka, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Coarse face/mouth term or animal muzzle; the policy leaves rude standalone language without a target unresolved.

### cs-x-fp-07 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Prdelka HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Little ass HD
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: The diminutive can be affectionate slang; the policy does not define when mild vulgarity becomes prohibited profanity.

### cs-x-fo-07 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `P.r.d.e.l.k.a HD`
- intended: same term as cs-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Little ass HD
- reviewer: label flag, category profanity, decoded Prdelka, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Vulgar diminutive can be affectionate or mildly cheeky; the policy leaves the boundary between profanity and mild slang open.

### cs-x-fp-09 - verified (flag / profanity / lexicon_plain)

- text: `Mrdka FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Cum / semen FM
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Vulgar term, also used as an insult.

### hu-x-fp-01 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Franc TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Damn / the devil TV
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Mild swearing or literal reference; the policy leaves a bare name's register boundary unresolved.

### hu-x-fo-01 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Fr4nc TV`
- intended: same term as hu-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Damn / the devil TV
- reviewer: label flag, category profanity, decoded Franc, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Mild curse or literal disease/devil reference; the policy leaves this standalone mild-swear boundary open.

### hu-x-fp-06 - disputed (flag / profanity / lexicon_plain)

- text: `Fing TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Fart TV
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Bodily slang without explicit sex or a target; the policy does not settle whether this alone is obscene or permitted mild slang.

### hu-x-fo-06 - disputed (flag / profanity / lexicon_obfuscated)

- text: `F1ng TV`
- intended: same term as hu-x-fp-06, disguised by code; technique: leet
- reviewer gloss: Fart TV
- reviewer: label clean, category none, decoded Fing, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-sexual bodily slang; the policy gives no boundary between this and obscene wording in a display name.

### hu-x-fp-07 - verified (flag / profanity / lexicon_plain)

- text: `Faszfejet HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Dickhead, in accusative form HD
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: The bare accusative sounds incomplete; standalone Faszfej is more natural.

### hu-x-fo-07 - verified (flag / profanity / lexicon_obfuscated)

- text: `F.a.s.z.f.e.j.e.t HD`
- intended: same term as hu-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Dickhead, in accusative form HD
- reviewer: label flag, category profanity, decoded Faszfejet, reading medium, label confidence high
- naturalness 2/3
- issue: The accusative is unmotivated in this isolated name; Faszfej would be the expected standalone noun.

### hu-x-fp-08 - verified (flag / profanity / lexicon_plain)

- text: `Leggecibb 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: The most asshole-like / shittiest 24
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Vulgar superlative derived from geci, semen / abusive jerk term.

### hu-x-fo-08 - verified (flag / profanity / lexicon_obfuscated)

- text: `Lеggесіbb 24`
- intended: same term as hu-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: The most asshole-like / shittiest 24
- reviewer: label flag, category profanity, decoded Leggecibb, reading medium, label confidence high
- issue: Vulgar superlative derived from geci, literally semen and also an abusive term.

### hu-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `Buksza FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Wallet / chick FM
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary wallet sense or coarse woman slang; the policy does not resolve a bare public name's use.

### hu-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Buuuksza FM`
- intended: same term as hu-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Wallet / chick FM
- reviewer: label clean, category none, decoded Buksza, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary wallet sense and coarse slang for a woman coexist; the policy does not resolve the bare name's context or register.

### hu-x-fp-10 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Francokat 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bollocks / no damn way 7
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Mild curse or dismissive expression; the policy does not define its boundary with permitted mild slang as a bare name.

### hu-x-fo-10 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Fr*ncokat 7`
- intended: same term as hu-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Bollocks / no damn way 7
- reviewer: label flag, category profanity, decoded Francokat, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Mild curse/dismissive exclamation; the policy does not define this boundary with permitted mild slang.

### sv-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `Moonade HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Mooned / showed a bare backside HD
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Describes non-graphic backside exposure; policy does not settle whether the mere reference is obscene.

### sv-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `M.o.o.n.a.d.e HD`
- intended: same term as sv-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Mooned / showed a bare backside HD
- reviewer: label clean, category none, decoded Moonade, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Loan verb describes non-graphic exposing of the backside; the policy does not settle whether mentioning it alone is obscene.

### sv-x-fp-08 - disputed (flag / profanity / lexicon_plain)

- text: `Brutta 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Chick / girl 24
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### sv-x-fo-08 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Bruttа 24`
- intended: same term as sv-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Chick / girl 24
- reviewer: label clean, category none, decoded Brutta, reading high, label confidence high
- label: intended flag, reviewer clean

### sv-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `Hård FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Hard / tough FM
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### sv-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Hååård FM`
- intended: same term as sv-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Hard / tough FM
- reviewer: label clean, category none, decoded Hård, reading high, label confidence high
- label: intended flag, reviewer clean

### sv-x-fp-10 - verified (flag / profanity / lexicon_plain)

- text: `Snefitta 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Crooked cunt 7
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Vulgar compound and insulting variant of snedfitta.

### sv-x-fo-10 - verified (flag / profanity / lexicon_obfuscated)

- text: `Sn*fitta 7`
- intended: same term as sv-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Crooked cunt 7
- reviewer: label flag, category profanity, decoded Snefitta, reading medium, label confidence high
- issue: Recognizable vulgar compound and insult.

### fi-x-fp-01 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Pentele TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Damn / darn TV
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Mild euphemistic curse; policy does not define its boundary with permitted mild slang in a targetless name.

### fi-x-fo-01 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `P3nt3l3 TV`
- intended: same term as fi-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Damn / darn TV
- reviewer: label flag, category profanity, decoded Pentele, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: A mild euphemistic curse; the policy does not specify when a standalone mild swear qualifies for the slang exception.

### fi-x-fp-06 - disputed (flag / profanity / lexicon_plain)

- text: `Viiksi TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Moustache TV
- reviewer: label clean, category none, decoded None, reading medium, label confidence high
- label: intended flag, reviewer clean

### fi-x-fo-06 - disputed (flag / profanity / lexicon_obfuscated)

- text: `V11k51 TV`
- intended: same term as fi-x-fp-06, disguised by code; technique: leet
- reviewer gloss: Moustache TV
- reviewer: label clean, category none, decoded Viiksi, reading medium, label confidence high
- label: intended flag, reviewer clean

### fi-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `Palli HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Stool / ball / testicle HD
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: An ordinary furniture noun and anatomical slang share the spelling; the policy does not resolve the contextless public name.

### fi-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `P.a.l.l.i HD`
- intended: same term as fi-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Stool / ball / testicle HD
- reviewer: label clean, category none, decoded Palli, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Furniture noun and anatomical slang readings coexist; the policy leaves contextless naming unresolved.

### fi-x-fp-08 - disputed (flag / profanity / lexicon_plain)

- text: `Lahtari 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Butcher / slaughterer 24
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Can describe a slaughterer or be a political insult; a bare word does not clearly glorify violence or demean an identified group.

### fi-x-fo-08 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Lаhtаrі 24`
- intended: same term as fi-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Butcher / slaughterer 24
- reviewer: label clean, category none, decoded Lahtari, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Can describe a slaughterer or serve as a political insult; the isolated name does not establish glorification or a group target.

### fi-x-fp-09 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Äpärä FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bastard FM
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Insulting or literal illegitimacy term without a target; the policy leaves standalone rude names unresolved.

### fi-x-fo-09 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Äpääärä FM`
- intended: same term as fi-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Bastard FM
- reviewer: label flag, category profanity, decoded Äpärä, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: An insulting word or literal birth-status term with no target; the policy does not resolve this standalone name.

### fi-x-fp-10 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Pallit 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Balls / testicles 7
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse anatomical slang or plural of stool; the policy does not determine a contextless name's sense or acceptability.

### fi-x-fo-10 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `P*llit 7`
- intended: same term as fi-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Balls / testicles 7
- reviewer: label flag, category profanity, decoded Pallit, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Also the plural of a stool; coarse anatomical slang and furniture readings are possible, which the policy does not resolve for a bare name.

### tr-x-fp-01 - verified (flag / profanity / lexicon_plain)

- text: `Götte TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: In the ass TV
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Locative case sounds fragmentary as a standalone name; Göt is the base noun.

### tr-x-fo-01 - verified (flag / profanity / lexicon_obfuscated)

- text: `Gött3 TV`
- intended: same term as tr-x-fp-01, disguised by code; technique: leet
- reviewer gloss: In the ass TV
- reviewer: label flag, category profanity, decoded Götte, reading medium, label confidence high
- naturalness 2/3
- issue: Isolated locative sounds incomplete; göt is the base noun.

### tr-x-fp-03 - verified (flag / profanity / lexicon_plain)

- text: `Sikte 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: In / on the dick 24
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Unmotivated standalone locative; sik is the base noun.

### tr-x-fo-03 - verified (flag / profanity / lexicon_obfuscated)

- text: `Sіktе 24`
- intended: same term as tr-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: In / on the dick 24
- reviewer: label flag, category profanity, decoded Sikte, reading medium, label confidence high
- naturalness 2/3
- issue: An unmotivated isolated locative; sik is the base noun.

### tr-x-fp-04 - verified (flag / profanity / lexicon_plain)

- text: `Sikleri FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Cocks / his cocks, inflected FM
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Unmotivated isolated accusative/possessive plural; sik is the base noun.

### tr-x-fo-04 - verified (flag / profanity / lexicon_obfuscated)

- text: `Siiikleri FM`
- intended: same term as tr-x-fp-04, disguised by code; technique: stretched
- reviewer gloss: Cocks / his cocks, inflected FM
- reviewer: label flag, category profanity, decoded Sikleri, reading medium, label confidence high
- naturalness 2/3
- issue: Isolated accusative/possessive plural sounds fragmentary; sik is the base noun.

### tr-x-fp-05 - verified (flag / profanity / lexicon_plain)

- text: `Yaraklara 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To cocks 7
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Unmotivated dative plural; the base noun is yarak.

### tr-x-fo-05 - verified (flag / profanity / lexicon_obfuscated)

- text: `Y*raklara 7`
- intended: same term as tr-x-fp-05, disguised by code; technique: masked
- reviewer gloss: To cocks 7
- reviewer: label flag, category profanity, decoded Yaraklara, reading medium, label confidence high
- naturalness 2/3
- issue: Unmotivated isolated dative plural; yarak is the base noun.

### tr-x-fp-06 - verified (flag / profanity / lexicon_plain)

- text: `Yarağa TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To the cock TV
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Isolated dative is fragmentary; yarak is the base noun.

### tr-x-fo-06 - verified (flag / profanity / lexicon_obfuscated)

- text: `Y4r4ğ4 TV`
- intended: same term as tr-x-fp-06, disguised by code; technique: leet
- reviewer gloss: To the cock TV
- reviewer: label flag, category profanity, decoded Yarağa, reading medium, label confidence high
- naturalness 2/3
- issue: Isolated dative is fragmentary; yarak is the base noun.

### tr-x-fp-07 - verified (flag / profanity / lexicon_plain)

- text: `Saksocuda HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: At the cocksucker's HD
- reviewer: label flag, category sexual, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Vulgar noun saksocu with a locative suffix; incomplete as a bare name.

### tr-x-fo-07 - verified (flag / profanity / lexicon_obfuscated)

- text: `S.a.k.s.o.c.u.d.a HD`
- intended: same term as tr-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: At the cocksucker's HD
- reviewer: label flag, category sexual, decoded Saksocuda, reading medium, label confidence high
- naturalness 2/3
- issue: Saksocu is the vulgar oral-sex performer noun; locative -da is awkward without surrounding context.

### tr-x-fp-08 - verified (flag / profanity / lexicon_plain)

- text: `Götvereni 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: The ass-giver / faggot, inflected 24
- reviewer: label flag, category hate, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Homophobic vulgar insult; isolated accusative/possessive form is awkward, base götveren.

### tr-x-fo-08 - verified (flag / profanity / lexicon_obfuscated)

- text: `Götvеrеnі 24`
- intended: same term as tr-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: The ass-giver / faggot, inflected 24
- reviewer: label flag, category hate, decoded Götvereni, reading medium, label confidence high
- naturalness 2/3
- issue: Homophobic vulgar insult; accusative/possessive form is awkward without context, base götveren.

### tr-x-fp-09 - verified (flag / profanity / lexicon_plain)

- text: `Göte FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To the ass FM
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Unmotivated isolated dative; göt is the base noun.

### tr-x-fo-09 - verified (flag / profanity / lexicon_obfuscated)

- text: `Göööte FM`
- intended: same term as tr-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: To the ass FM
- reviewer: label flag, category profanity, decoded Göte, reading medium, label confidence high
- naturalness 2/3
- issue: Isolated dative is fragmentary; göt is the base noun.

### tr-x-fp-10 - verified (flag / profanity / lexicon_plain)

- text: `Sike 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: To the dick 7
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: Unmotivated isolated dative; sik is the base noun.

### tr-x-fo-10 - verified (flag / profanity / lexicon_obfuscated)

- text: `S*ke 7`
- intended: same term as tr-x-fp-10, disguised by code; technique: masked
- reviewer gloss: To the dick 7
- reviewer: label flag, category profanity, decoded Sike, reading medium, label confidence medium
- naturalness 2/3
- issue: Sike is a plausible vulgar completion; the isolated dative sounds incomplete, base sik. Other completions of the mask are possible.

### vi-x-fp-01 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Chết mịe TV`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Fucking dead / oh shit TV
- reviewer: label flag, category profanity, decoded chết mẹ, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Euphemistic spelling of a crude exclamation; the policy leaves the mild-slang versus profanity boundary open.

### vi-x-fo-01 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Chết mị3 TV`
- intended: same term as vi-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Fucking dead / oh shit TV
- reviewer: label flag, category profanity, decoded chết mẹ, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: A softened spelling of a crude exclamation; the policy does not define when euphemistic swearing becomes permitted mild slang.

### vi-x-fp-02 - verified (flag / profanity / lexicon_plain)

- text: `Đê mờ HD`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Fuck mother HD
- reviewer: label flag, category profanity, decoded địt mẹ, reading medium, label confidence high
- issue: Spoken letter names for the abbreviated curse đm.

### vi-x-fo-02 - verified (flag / profanity / lexicon_obfuscated)

- text: `Đ.ê m.ờ HD`
- intended: same term as vi-x-fp-02, disguised by code; technique: spaced
- reviewer gloss: Fuck mother HD
- reviewer: label flag, category profanity, decoded địt mẹ, reading medium, label confidence high
- issue: Pronounced names of the letters Đ and M stand for the profanity đm.

### vi-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `Occho 24`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Dog brain / idiot 24
- reviewer: label clean, category none, decoded óc chó, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Targetless insulting name; the policy does not say when it becomes harassment.

### vi-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Оссhо 24`
- intended: same term as vi-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Dog brain / idiot 24
- reviewer: label clean, category none, decoded óc chó, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Insult used as a targetless name; the policy does not define the boundary between rude slang and harassment.

### vi-x-fp-05 - verified (flag / profanity / lexicon_plain)

- text: `Đủ mé 7`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Fuck mother 7
- reviewer: label flag, category profanity, decoded đụ mẹ, reading medium, label confidence high
- issue: Recognizable euphemistic/altered spelling of the curse.

### vi-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `Buoi HD`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Grapefruit / session / cock HD
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Untoned buoi can be ordinary bưởi or buổi, or vulgar buồi; no unique decoding and no policy rule for the ambiguous bare name.

### vi-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `B.u.o.i HD`
- intended: same term as vi-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Grapefruit / session / cock HD
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Without tone marks buoi can represent bưởi, buổi or vulgar buồi; I cannot uniquely decode it. The policy gives no rule for this ambiguous public name.

### vi-x-fp-08 - reading_low (flag / profanity / lexicon_plain)

- text: `Mát lol 24`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Cool / soothed pussy 24
- reviewer: label flag, category profanity, decoded mát lồn, reading low, label confidence high
- reviewer reads this item poorly
- issue: I recognize lol as an evasion of lồn, but the phrase's exact idiomatic tone is uncertain; literal gloss preserves the readable words.

### vi-x-fo-08 - reading_low (flag / profanity / lexicon_obfuscated)

- text: `Mát lоl 24`
- intended: same term as vi-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Cool / soothed pussy 24
- reviewer: label flag, category profanity, decoded mát lồn, reading low, label confidence high
- reviewer reads this item poorly
- issue: Recognizable substitution of lol for lồn; I am less certain of the exact idiomatic meaning of the phrase.

### vi-x-fp-09 - verified (flag / profanity / lexicon_plain)

- text: `Đmmmm FM`
- intended: term sampled from vietnamese-offensive-words; flagged by list membership, no gloss
- reviewer gloss: Fuck mother FM
- reviewer: label flag, category profanity, decoded địt mẹ, reading medium, label confidence high
- issue: Extended abbreviation đm.

### vi-x-fo-09 - verified (flag / profanity / lexicon_obfuscated)

- text: `Đmmmmmm FM`
- intended: same term as vi-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Fuck mother FM
- reviewer: label flag, category profanity, decoded địt mẹ, reading medium, label confidence high
- issue: Stretched abbreviation đm.

### ru-x-fp-06 - disputed (flag / profanity / lexicon_plain)

- text: `Хрен TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Horseradish / dick euphemism TV
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary vegetable or coarse euphemism; the policy does not determine the reading of a contextless public name.

### ru-x-fo-06 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Х.р.е.н TV`
- intended: same term as ru-x-fp-06, disguised by code; technique: spaced
- reviewer gloss: Horseradish / dick euphemism TV
- reviewer: label clean, category none, decoded Хрен, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: An ordinary vegetable word and coarse euphemism coexist; the policy does not resolve the isolated name.

### ru-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `Офигеть FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Wow / holy cow FM
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: Common softened exclamation of surprise without a target or overt obscenity.

### ru-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Офииигеть FM`
- intended: same term as ru-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Wow / holy cow FM
- reviewer: label clean, category none, decoded Офигеть, reading high, label confidence high
- label: intended flag, reviewer clean
- issue: A softened everyday exclamation of surprise, with no target or explicit content.

### ru-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `Голый 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Naked 7
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic undress adjective; policy leaves the boundary for contextless public naming unresolved.

### ru-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `Г*лый 7`
- intended: same term as ru-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Naked 7
- reviewer: label clean, category none, decoded Голый, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic undress adjective; the policy does not settle whether such contextless public names are sexual enough to flag.

### ar-x-fp-01 - verified (flag / profanity / lexicon_plain)

- text: `خول TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Faggot TV
- reviewer: label flag, category hate, decoded None, reading medium, label confidence high
- issue: Egyptian derogatory slur for a gay or effeminate man.

### ar-x-fo-01 - verified (flag / profanity / lexicon_obfuscated)

- text: `خ.و.ل TV`
- intended: same term as ar-x-fp-01, disguised by code; technique: spaced
- reviewer gloss: Faggot TV
- reviewer: label flag, category hate, decoded خول, reading medium, label confidence high
- issue: Egyptian derogatory slur for a gay or effeminate man.

### ar-x-fp-02 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `سحاق HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Lesbian sexual intercourse HD
- reviewer: label flag, category sexual, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: The policy does not specify whether a non-graphic sexual term alone is explicit enough to flag.

### ar-x-fo-02 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `سحا* HD`
- intended: same term as ar-x-fp-02, disguised by code; technique: masked
- reviewer gloss: Lesbian sexual intercourse HD
- reviewer: label flag, category sexual, decoded سحاق, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: The policy does not specify whether a non-graphic sexual term alone is explicit enough to flag.

### ar-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `فرج 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Relief / Faraj / vulva 24
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: This is also an ordinary word and personal name; the policy does not determine which sense a bare name invokes.

### ar-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `فرررج 24`
- intended: same term as ar-x-fp-03, disguised by code; technique: stretched
- reviewer gloss: Relief / Faraj / vulva 24
- reviewer: label clean, category none, decoded فرج, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Plausible personal-name and ordinary readings compete with an anatomical one; the policy gives no rule for this contextless ambiguity.

### ar-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `شاذ FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Deviant / irregular / homosexual FM
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: The isolated adjective can be ordinary or a derogatory description of gay people; the policy does not resolve the contextless use.

### ar-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `ش.ا.ذ FM`
- intended: same term as ar-x-fp-04, disguised by code; technique: spaced
- reviewer gloss: Deviant / irregular / homosexual FM
- reviewer: label clean, category none, decoded شاذ, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: This can be an ordinary adjective or a derogatory label for gay people; the isolated name does not establish a target or sense.

### ar-x-fp-06 - verified (flag / profanity / lexicon_plain)

- text: `لوطي TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Sodomite TV
- reviewer: label flag, category hate, decoded None, reading medium, label confidence high
- issue: Derogatory label for gay men.

### ar-x-fo-06 - verified (flag / profanity / lexicon_obfuscated)

- text: `لوووطي TV`
- intended: same term as ar-x-fp-06, disguised by code; technique: stretched
- reviewer gloss: Sodomite TV
- reviewer: label flag, category hate, decoded لوطي, reading medium, label confidence high
- issue: Derogatory term for a gay man; extended letters decoded.

### ar-x-fp-07 - disputed (flag / profanity / lexicon_plain)

- text: `مبادل HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Exchanger / someone who exchanges HD
- reviewer: label clean, category none, decoded None, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: I recognize the ordinary participle; I cannot confirm any dialectal sexual slang reading from this isolated name.

### ar-x-fo-07 - disputed (flag / profanity / lexicon_obfuscated)

- text: `م.ب.ا.د.ل HD`
- intended: same term as ar-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Exchanger / someone who exchanges HD
- reviewer: label clean, category none, decoded مبادل, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: Ordinary participle is readable; I cannot confirm a dialectal sexual sense here.

### ar-x-fp-08 - verified (flag / profanity / lexicon_plain)

- text: `عرص 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Pimp / cuckold / scumbag 24
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence high
- issue: Vulgar dialectal insult; exact English equivalent varies.

### ar-x-fp-09 - disputed (flag / profanity / lexicon_plain)

- text: `شهوة FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Desire / lust FM
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Not a graphic sexual description, but the policy leaves contextless sexualized names underspecified.

### ar-x-fo-09 - disputed (flag / profanity / lexicon_obfuscated)

- text: `شهههوة FM`
- intended: same term as ar-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Desire / lust FM
- reviewer: label clean, category none, decoded شهوة, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Desire alone is not explicit sexual content, but its acceptability as a contextless public name is underspecified.

### ar-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `بظر 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Clitoris 7
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: The policy does not resolve isolated anatomical terms without medical or sexual context.

### ar-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `ب.ظ.ر 7`
- intended: same term as ar-x-fp-10, disguised by code; technique: spaced
- reviewer gloss: Clitoris 7
- reviewer: label clean, category none, decoded بظر, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: An anatomical term alone is not a sexual description; the policy does not specify treatment of such public names without medical context.

### hi-x-fp-01 - disputed (flag / profanity / lexicon_plain)

- text: `Pataka TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Firecracker / attractive woman TV
- reviewer: label clean, category none, decoded पटाखा, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: Can be ordinary noun or mild appreciative slang; no explicit sexual content or abusive target.

### hi-x-fo-01 - disputed (flag / profanity / lexicon_obfuscated)

- text: `P4t4k4 TV`
- intended: same term as hi-x-fp-01, disguised by code; technique: leet
- reviewer gloss: Firecracker / attractive woman TV
- reviewer: label clean, category none, decoded पटाखा, reading medium, label confidence high
- label: intended flag, reviewer clean

### hi-x-fp-03 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Choochi 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Tit / nipple 24
- reviewer: label flag, category profanity, decoded चूची, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse anatomy word without explicit action; the policy leaves this standalone slang name unresolved.

### hi-x-fo-03 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Сhоосhі 24`
- intended: same term as hi-x-fp-03, disguised by code; technique: homoglyph
- reviewer gloss: Tit / nipple 24
- reviewer: label flag, category profanity, decoded चूची, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Anatomical slang without explicit action; the policy does not resolve its boundary with mild slang in a bare name.

### hi-x-fp-06 - verified (flag / profanity / lexicon_plain)

- text: `Gaandfat TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Ass-torn / scared shitless TV
- reviewer: label flag, category profanity, decoded गांडफट, reading medium, label confidence high
- issue: Coarse compound used of a coward; precise spelling varies online.

### hi-x-fo-06 - verified (flag / profanity / lexicon_obfuscated)

- text: `G44ndf4t TV`
- intended: same term as hi-x-fp-06, disguised by code; technique: leet
- reviewer gloss: Ass-torn / scared shitless TV
- reviewer: label flag, category profanity, decoded गांडफट, reading medium, label confidence high
- issue: Vulgar compound used of a coward; online Roman spelling varies.

### hi-x-fp-07 - reading_low (flag / profanity / lexicon_plain)

- text: `Aandu HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Balls / testicle-derived insult HD
- reviewer: label flag, category profanity, decoded आंडू, reading low, label confidence high
- reviewer reads this item poorly
- issue: I recognize a vulgar slang form related to testicles, but am uncertain about its exact register and Hindi/Punjabi usage.

### hi-x-fo-07 - reading_low (flag / profanity / lexicon_obfuscated)

- text: `A.a.n.d.u HD`
- intended: same term as hi-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Balls / testicle-derived insult HD
- reviewer: label flag, category profanity, decoded आंडू, reading low, label confidence high
- reviewer reads this item poorly
- issue: I recognize a vulgar testicle-derived slang form, but am uncertain about its precise Hindi/Punjabi register and English equivalent.

### hi-x-fp-08 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Kamine 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Scoundrels / bastards 24
- reviewer: label flag, category profanity, decoded कमीने, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: An insulting word with no target; policy leaves the boundary between non-profane rudeness and harassment open.

### hi-x-fo-08 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Kаmіnе 24`
- intended: same term as hi-x-fp-08, disguised by code; technique: homoglyph
- reviewer gloss: Scoundrels / bastards 24
- reviewer: label flag, category profanity, decoded कमीने, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Targetless insulting word; the policy does not specify whether this register is profane enough in a display name.

### hi-x-fp-09 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Chuche FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Tits / nipples FM
- reviewer: label flag, category profanity, decoded चूचे, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse anatomy word; the policy does not specify whether this standalone name is obscenity or permitted mild slang.

### hi-x-fo-09 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `Chuuuche FM`
- intended: same term as hi-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Tits / nipples FM
- reviewer: label flag, category profanity, decoded चूचे, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse anatomical slang, not a sexual act; the policy does not define the mild-slang versus obscenity boundary here.

### hi-x-fp-10 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `Kuttiya 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bitch / female dog 7
- reviewer: label flag, category profanity, decoded कुतिया, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Literal animal and abusive readings coexist; no target or breeding context settles the bare name.

### hi-x-fo-10 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `K*ttiya 7`
- intended: same term as hi-x-fp-10, disguised by code; technique: masked
- reviewer gloss: Bitch / female dog 7
- reviewer: label flag, category profanity, decoded कुतिया, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Transliterated female-dog word can be abusive or literal; the policy does not settle the isolated name. A hut would normally be कुटिया.

### th-x-fp-01 - disputed (flag / profanity / lexicon_plain)

- text: `กะปิ TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Shrimp paste TV
- reviewer: label clean, category none, decoded None, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: Ordinary food word; I cannot establish a sexual slang meaning from this text alone.

### th-x-fo-01 - disputed (flag / profanity / lexicon_obfuscated)

- text: `ก.ะ.ปิ TV`
- intended: same term as th-x-fp-01, disguised by code; technique: spaced
- reviewer gloss: Shrimp paste TV
- reviewer: label clean, category none, decoded กะปิ, reading medium, label confidence high
- label: intended flag, reviewer clean
- issue: Ordinary food word; no established sexual context here.

### th-x-fp-02 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `น้ําแตก HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Ejaculation / water bursting HD
- reviewer: label flag, category sexual, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Colloquial ejaculation sense and literal water-release readings are possible; the policy does not resolve the bare name.

### th-x-fo-02 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `น้ําแต* HD`
- intended: same term as th-x-fp-02, disguised by code; technique: masked
- reviewer gloss: Ejaculation / water bursting HD
- reviewer: label flag, category sexual, decoded น้ำแตก, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Sexual slang and literal water-release senses coexist; the policy does not resolve the contextless name.

### th-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `หลั่ง 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Flow / secrete / ejaculate 24
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary and sexual meanings coexist; policy does not settle the isolated name.

### th-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `หลั่ลั่ลั่ง 24`
- intended: same term as th-x-fp-03, disguised by code; technique: stretched
- reviewer gloss: Flow / secrete / ejaculate 24
- reviewer: label clean, category none, decoded หลั่ง, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary secretion verb also has a sexual sense; the bare name does not settle the policy application.

### th-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `เจี๊ยว FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Willy / penis FM
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Childish anatomy term; the policy leaves the mild-slang versus obscenity boundary open in a contextless name.

### th-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `เ.จี๊.ย.ว FM`
- intended: same term as th-x-fp-04, disguised by code; technique: spaced
- reviewer gloss: Willy / penis FM
- reviewer: label clean, category none, decoded เจี๊ยว, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Childish anatomical slang without an explicit act; the policy does not resolve whether such a bare name is obscene or mild.

### th-x-fp-05 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `เหี้ย 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Monitor lizard / fuck / bastard 7
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Animal noun widely used as a strong curse; the policy cannot settle a contextless name's sense.

### th-x-fo-05 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `เหี้* 7`
- intended: same term as th-x-fp-05, disguised by code; technique: masked
- reviewer gloss: Monitor lizard / fuck / bastard 7
- reviewer: label flag, category profanity, decoded เหี้ย, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Literal animal and profanity readings coexist; the isolated name is unresolved by the policy.

### th-x-fp-08 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `ไอ้ควาย 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: You buffalo / idiot 24
- reviewer: label flag, category harassment, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: A coarse insult used as a targetless display name; policy does not settle whether that constitutes harassment.

### th-x-fo-08 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `ไอ้ควา* 24`
- intended: same term as th-x-fp-08, disguised by code; technique: masked
- reviewer gloss: You buffalo / idiot 24
- reviewer: label flag, category harassment, decoded ไอ้ควาย, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Coarse targetless insult; the policy does not define the name's rudeness/harassment boundary.

### th-x-fp-09 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `หญิงชาติชั่ว FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Wicked / vile woman FM
- reviewer: label flag, category harassment, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Demeaning gendered insult with no identifiable personal target; the policy leaves the rude-name versus harassment boundary open.

### th-x-fo-09 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `หญิญิญิงชาติชั่ว FM`
- intended: same term as th-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Wicked / vile woman FM
- reviewer: label flag, category harassment, decoded หญิงชาติชั่ว, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: A demeaning gendered insult without a specific target; policy does not define the boundary with harassment.

### th-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `ล้างตู้เย็น 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Wash the refrigerator 7
- reviewer: label clean, category none, decoded None, reading low, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- reviewer reads this item poorly
- issue: Literal cleaning phrase with a possible sexual slang reading; my Thai slang knowledge is limited and the bare name does not establish the sense.

### th-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `ล้.า.ง.ตู้.เ.ย็.น 7`
- intended: same term as th-x-fp-10, disguised by code; technique: spaced
- reviewer gloss: Wash the refrigerator 7
- reviewer: label clean, category none, decoded ล้างตู้เย็น, reading low, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- reviewer reads this item poorly
- issue: I recognize the literal household phrase and a possible cunnilingus slang use, but my Thai slang reading is limited; the contextless phrase does not settle policy application.

### ja-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `ローター HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Rotor / vibrator HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary mechanical noun also used for a sex toy; the bare name does not determine which reading applies under the policy.

### ja-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `ロータ* HD`
- intended: same term as ja-x-fp-02, disguised by code; technique: masked
- reviewer gloss: Rotor / vibrator HD
- reviewer: label clean, category none, decoded ローター, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Mechanical and sex-toy senses coexist; the policy does not resolve a contextless public name.

### ja-x-fp-03 - disputed (flag / profanity / lexicon_plain)

- text: `エロティック 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Erotic 24
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Suggestive adjective without an explicit sexual act; the policy leaves such standalone names unresolved.

### ja-x-fo-03 - disputed (flag / profanity / lexicon_obfuscated)

- text: `エロロロティック 24`
- intended: same term as ja-x-fp-03, disguised by code; technique: stretched
- reviewer gloss: Erotic 24
- reviewer: label clean, category none, decoded エロティック, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Suggestive adjective without explicit acts; the policy does not resolve such a bare name.

### ja-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `トップレス FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Topless FM
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Names non-graphic undress; the policy does not define whether this alone is sexual explicitness.

### ja-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `ト.ッ.プ.レ.ス FM`
- intended: same term as ja-x-fp-04, disguised by code; technique: spaced
- reviewer gloss: Topless FM
- reviewer: label clean, category none, decoded トップレス, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic undress term; the policy leaves the boundary with sexual explicitness open.

### ja-x-fp-05 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `エッチ 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Sex / lewd / H 7
- reviewer: label flag, category sexual, decoded None, reading high, label confidence medium
- reviewer says the policy does not settle this item
- issue: Colloquial sexual sense and the letter H are possible; the policy does not settle the isolated name's reading or explicitness.

### ja-x-fo-05 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `エッ* 7`
- intended: same term as ja-x-fp-05, disguised by code; technique: masked
- reviewer gloss: Sex / lewd / H 7
- reviewer: label flag, category sexual, decoded エッチ, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: The mask could cover another completion, but エッチ is a plausible reading; even decoded, explicitness of the standalone term is unresolved.

### ja-x-fp-06 - verified (flag / profanity / lexicon_plain)

- text: `騎上位 TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Cowgirl sexual position TV
- reviewer: label flag, category sexual, decoded None, reading medium, label confidence high
- naturalness 2/3
- issue: The recognizable intended term is 騎乗位; 騎上位 uses the wrong middle character and is not the standard spelling.

### ja-x-fo-06 - verified (flag / profanity / lexicon_obfuscated)

- text: `騎上上上位 TV`
- intended: same term as ja-x-fp-06, disguised by code; technique: stretched
- reviewer gloss: Cowgirl sexual position TV
- reviewer: label flag, category sexual, decoded 騎上位, reading medium, label confidence high
- naturalness 2/3
- issue: After repetition is removed the spelling is still nonstandard; the conventional term is 騎乗位.

### ja-x-fp-08 - disputed (flag / profanity / lexicon_plain)

- text: `剃毛 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Shaving body hair 24
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### ja-x-fo-08 - disputed (flag / profanity / lexicon_obfuscated)

- text: `剃* 24`
- intended: same term as ja-x-fp-08, disguised by code; technique: masked
- reviewer gloss: Shaving body hair 24
- reviewer: label clean, category none, decoded 剃毛, reading medium, label confidence medium
- label: intended flag, reviewer clean
- issue: 剃毛 is a plausible completion of 剃*, but other shaving compounds are possible; none is established as sexual here.

### ja-x-fp-10 - disputed (flag / profanity / lexicon_plain)

- text: `エスコート 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Escort / accompanying someone 7
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### ja-x-fo-10 - disputed (flag / profanity / lexicon_obfuscated)

- text: `エ.ス.コ.ー.ト 7`
- intended: same term as ja-x-fp-10, disguised by code; technique: spaced
- reviewer gloss: Escort / accompanying someone 7
- reviewer: label clean, category none, decoded エスコート, reading high, label confidence high
- label: intended flag, reviewer clean

### ko-x-co-02 - verified (clean / none / control_obfuscated)

- text: `부* 낚시 일기`
- intended: clean name ko-s-cp-02 with one word disguised by code; technique: masked
- reviewer gloss: Busan fishing diary
- reviewer: label clean, category none, decoded 부산, reading medium, label confidence medium
- issue: Busan is a plausible place-name completion of 부*, though not uniquely recoverable.

### ko-x-fp-01 - disputed (flag / profanity / lexicon_plain)

- text: `육갑 TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Sixty-year cycle / foolish antics TV
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: A traditional calendrical term also occurs in rude expressions; the policy does not settle its isolated public-name use.

### ko-x-fo-01 - disputed (flag / profanity / lexicon_obfuscated)

- text: `육.갑 TV`
- intended: same term as ko-x-fp-01, disguised by code; technique: spaced
- reviewer gloss: Sixty-year cycle / foolish antics TV
- reviewer: label clean, category none, decoded 육갑, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Calendar noun or rude expression; the policy leaves this contextless use unresolved.

### ko-x-fp-02 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `암캐 HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bitch / female dog HD
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Literal animal noun and abusive human sense coexist; the bare public name has no context to settle application of the policy.

### ko-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `유모 FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Wet nurse / nanny FM
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary noun also used as an abbreviation in pornography for censored material; the policy does not determine the sense of a contextless name.

### ko-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `유.모 FM`
- intended: same term as ko-x-fp-04, disguised by code; technique: spaced
- reviewer gloss: Wet nurse / nanny FM
- reviewer: label clean, category none, decoded 유모, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Ordinary noun and pornography abbreviation coexist; the policy does not determine which sense applies to this name.

### ko-x-fp-05 - verified (flag / profanity / lexicon_plain)

- text: `애자 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Retard 7
- reviewer: label flag, category hate, decoded None, reading medium, label confidence high
- issue: Derogatory abbreviated disability term used as an insult.

### ko-x-fp-06 - disputed (flag / profanity / lexicon_plain)

- text: `에로 TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Erotic / erotica TV
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Suggestive sexual-topic word without explicit acts; the policy does not resolve the standalone-name boundary.

### ko-x-fo-06 - disputed (flag / profanity / lexicon_obfuscated)

- text: `에로로로 TV`
- intended: same term as ko-x-fp-06, disguised by code; technique: stretched
- reviewer gloss: Erotic / erotica TV
- reviewer: label clean, category none, decoded 에로, reading medium, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic sexual-topic word; policy leaves its acceptability as a bare name unresolved.

### ko-x-fp-08 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `후레아들 24`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Bastard / ill-bred son 24
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: An insulting non-explicit word without a target; policy does not define its boundary with prohibited profanity or harassment.

### ko-x-fo-08 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `후레아* 24`
- intended: same term as ko-x-fp-08, disguised by code; technique: masked
- reviewer gloss: Bastard / ill-bred son 24
- reviewer: label flag, category profanity, decoded 후레아들, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Insulting non-explicit word without a target; the policy leaves its profanity/harassment boundary unresolved.

### ko-x-fp-09 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `딸딸이 FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Jerking off FM
- reviewer: label flag, category sexual, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Masturbation slang also has nonsexual regional uses; the bare name does not settle the reading.

### ko-x-fo-09 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `딸딸딸딸이 FM`
- intended: same term as ko-x-fp-09, disguised by code; technique: stretched
- reviewer gloss: Jerking off FM
- reviewer: label flag, category sexual, decoded 딸딸이, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Usual sexual slang also has regional nonsexual object/vehicle uses; the policy does not settle a contextless name.

### ko-x-fp-10 - verified (flag / profanity / lexicon_plain)

- text: `씹빨 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Fuck 7
- reviewer: label flag, category profanity, decoded 씨발, reading medium, label confidence high
- issue: Vulgar respelling 씹빨 is recognizable.

### ko-x-fo-10 - verified (flag / profanity / lexicon_obfuscated)

- text: `씹.빨 7`
- intended: same term as ko-x-fp-10, disguised by code; technique: spaced
- reviewer gloss: Fuck 7
- reviewer: label flag, category profanity, decoded 씨발, reading medium, label confidence high
- issue: Dotted 씹빨, a recognizable vulgar respelling.

### zh-x-co-05 - verified (clean / none / control_obfuscated)

- text: `小白学编*`
- intended: clean name zh-s-cp-05 with one word disguised by code; technique: masked
- reviewer gloss: A beginner learns programming / weaving
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- issue: The masked 编* could be 编程 or 编织; I cannot uniquely decode it, but the readable phrase is ordinary learning content.

### zh-x-fp-01 - reading_low (flag / profanity / lexicon_plain)

- text: `懒八 TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Balls / scrotum TV
- reviewer: label flag, category profanity, decoded 懶趴, reading low, label confidence high
- reviewer reads this item poorly
- issue: Likely homophonic Taiwanese genital slang; this spelling is nonstandard and my Taiwanese slang reading is limited.

### zh-x-fo-01 - reading_low (flag / profanity / lexicon_obfuscated)

- text: `懒.八 TV`
- intended: same term as zh-x-fp-01, disguised by code; technique: spaced
- reviewer gloss: Balls / scrotum TV
- reviewer: label flag, category profanity, decoded 懶趴, reading low, label confidence high
- reviewer reads this item poorly
- issue: I recognize a likely Taiwanese slang/homophonic scrotum term, but 懒八 is not a standard written form and my command of Taiwanese slang is limited.

### zh-x-fp-02 - disputed (flag / profanity / lexicon_plain)

- text: `小乳头 HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Little nipple HD
- reviewer: label clean, category none, decoded None, reading high, label confidence medium
- label: intended flag, reviewer clean
- reviewer says the policy does not settle this item
- issue: Non-graphic anatomical noun without medical context; the policy does not resolve this bare public name.

### zh-x-fo-02 - disputed (flag / profanity / lexicon_obfuscated)

- text: `小乳* HD`
- intended: same term as zh-x-fp-02, disguised by code; technique: masked
- reviewer gloss: Little breast/milk... HD
- reviewer: label clean, category none, decoded None, reading medium, label confidence medium
- label: intended flag, reviewer clean
- issue: 小乳* is incomplete: nipple and other breast-related completions are possible. I cannot uniquely decode it and judge only the non-graphic readable fragment.

### zh-x-fp-04 - disputed (flag / profanity / lexicon_plain)

- text: `激情 FM`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Passion FM
- reviewer: label clean, category none, decoded None, reading high, label confidence high
- label: intended flag, reviewer clean

### zh-x-fo-04 - disputed (flag / profanity / lexicon_obfuscated)

- text: `激.情 FM`
- intended: same term as zh-x-fp-04, disguised by code; technique: spaced
- reviewer gloss: Passion FM
- reviewer: label clean, category none, decoded 激情, reading high, label confidence high
- label: intended flag, reviewer clean

### zh-x-fp-05 - verified (flag / profanity / lexicon_plain)

- text: `你它妈的 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: You fucking... / your mother's... 7
- reviewer: label flag, category profanity, decoded 你他妈的, reading high, label confidence high
- issue: 它 is substituted for 他 in a recognizable curse phrase.

### zh-x-fo-05 - verified (flag / profanity / lexicon_obfuscated)

- text: `你它妈* 7`
- intended: same term as zh-x-fp-05, disguised by code; technique: masked
- reviewer gloss: You fucking... / your mother's... 7
- reviewer: label flag, category profanity, decoded 你他妈的, reading high, label confidence high
- issue: Pronoun substitution and masked final particle in the recognizable curse.

### zh-x-fp-06 - policy_ambiguous (flag / profanity / lexicon_plain)

- text: `奶奶的熊 TV`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Grandma's bear / damn it TV
- reviewer: label flag, category profanity, decoded None, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: An established softened curse also has a literal innocent possessive reading; the policy leaves the euphemistic mild-slang boundary open.

### zh-x-fo-06 - policy_ambiguous (flag / profanity / lexicon_obfuscated)

- text: `奶奶奶奶的熊 TV`
- intended: same term as zh-x-fp-06, disguised by code; technique: stretched
- reviewer gloss: Grandma's bear / damn it TV
- reviewer: label flag, category profanity, decoded 奶奶的熊, reading medium, label confidence medium
- reviewer says the policy does not settle this item
- issue: Softened curse or literal grandmother's bear; policy leaves the mild-slang boundary and isolated sense unresolved.

### zh-x-fp-07 - verified (flag / profanity / lexicon_plain)

- text: `几芭 HD`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Dick HD
- reviewer: label flag, category profanity, decoded 鸡巴, reading high, label confidence high
- issue: Near-homophonic character substitutions retain a recognizable vulgar word.

### zh-x-fo-07 - verified (flag / profanity / lexicon_obfuscated)

- text: `几.芭 HD`
- intended: same term as zh-x-fp-07, disguised by code; technique: spaced
- reviewer gloss: Dick HD
- reviewer: label flag, category profanity, decoded 鸡巴, reading high, label confidence high
- issue: Dotted near-homophonic substitute characters for a recognizable vulgar word.

### zh-x-fp-10 - verified (flag / profanity / lexicon_plain)

- text: `干你良 7`
- intended: term sampled from LDNOOBW; flagged by list membership, no gloss
- reviewer gloss: Fuck your mother 7
- reviewer: label flag, category profanity, decoded 干你娘, reading high, label confidence high
- issue: 良 is a near-homophonic substitution for 娘 in the recognizable curse.

### zh-x-fo-10 - verified (flag / profanity / lexicon_obfuscated)

- text: `干.你.良 7`
- intended: same term as zh-x-fp-10, disguised by code; technique: spaced
- reviewer gloss: Fuck your mother 7
- reviewer: label flag, category profanity, decoded 干你娘, reading high, label confidence high
- issue: Dotted near-homophonic substitution 良 for 娘.
