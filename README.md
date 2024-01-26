Convert Benglai Text to English Phonetic Using Bengali IPA API. ( Source: https://ipa.bangla.gov.bd/ )

```bash
>>> from b2e import b2e

>>> b2e("আমার সোনার বাংলা আমি তোমায় ভালোবাসি")
'amar sonar banla ami tomay bhalobasi'

>>> b2e("আমার সোনার বাংলা আমি তোমায় ভালোবাসি", ipa=True)
'amar ʃonar baŋla ami t̪omaʲ bʱalobaʃi'
```
