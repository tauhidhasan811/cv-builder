
PRECEDENT_CASES = [
    # Tort - Negligence
    ("Donoghue v Stevenson [1932] AC 562", "tort law - negligence", "food and beverage manufacturing"),
    ("Caparo Industries plc v Dickman [1990] 2 AC 605", "tort law - negligence", "financial services and auditing"),
    ("Hedley Byrne & Co Ltd v Heller & Partners Ltd [1964] AC 465", "tort law - economic loss", "banking and financial advice"),
    ("Bolton v Stone [1951] AC 850", "tort law - negligence", "sports and leisure"),
    ("Paris v Stepney Borough Council [1951] AC 367", "tort law - negligence", "local government and public services"),
    ("Barnett v Chelsea & Kensington Hospital [1969] 1 QB 428", "tort law - negligence", "healthcare and medical services"),

    # Tort - Psychiatric Injury
    ("Alcock v Chief Constable of South Yorkshire [1992] 1 AC 310", "tort law - psychiatric injury", "emergency and public services"),
    ("Page v Smith [1996] AC 155", "tort law - psychiatric injury", "transport and road safety"),
    ("White v Chief Constable of South Yorkshire [1999] 2 AC 455", "tort law - psychiatric injury", "emergency and public services"),

    # Tort - Occupiers Liability
    ("Wheat v E Lacon & Co Ltd [1966] AC 552", "tort law - occupiers liability", "hospitality and accommodation"),
    ("Tomlinson v Congleton Borough Council [2003] UKHL 47", "tort law - occupiers liability", "local government and leisure"),
    ("Revill v Newbery [1996] QB 567", "tort law - occupiers liability", "residential property"),

    # Tort - Vicarious Liability
    ("Lister v Hesley Hall Ltd [2001] UKHL 22", "tort law - vicarious liability", "education and care services"),
    ("Various Claimants v Catholic Child Welfare Society [2012] UKSC 56", "tort law - vicarious liability", "education and charitable organisations"),
    ("Mohamud v WM Morrison Supermarkets plc [2016] UKSC 11", "tort law - vicarious liability", "retail and supermarkets"),

    # Tort - Nuisance
    ("Rylands v Fletcher [1868] LR 3 HL 330", "tort law - nuisance", "industrial and utilities"),
    ("Cambridge Water Co v Eastern Counties Leather [1994] 2 AC 264", "tort law - nuisance", "manufacturing and environmental"),
    ("Hunter v Canary Wharf Ltd [1997] AC 655", "tort law - nuisance", "construction and property development"),

    # Tort - Defamation
    ("Reynolds v Times Newspapers Ltd [2001] 2 AC 127", "tort law - defamation", "media and publishing"),

    # Contract - Offer and Acceptance
    ("Carlill v Carbolic Smoke Ball Co [1893] 1 QB 256", "contract law - offer and acceptance", "pharmaceutical and consumer products"),
    ("Byrne v Van Tienhoven [1880] 5 CPD 344", "contract law - offer and acceptance", "international trade and commerce"),
    ("Hyde v Wrench [1840] 3 Beav 334", "contract law - offer and acceptance", "real estate and property"),

    # Contract - Consideration
    ("Currie v Misa [1875] LR 10 Ex 153", "contract law - consideration", "commercial and business services"),
    ("Williams v Roffey Bros & Nicholls Ltd [1991] 1 QB 1", "contract law - consideration", "construction and property development"),
    ("Foakes v Beer [1884] 9 App Cas 605", "contract law - consideration", "financial services and debt recovery"),

    # Contract - Intention
    ("Balfour v Balfour [1919] 2 KB 571", "contract law - intention to create legal relations", "domestic and family arrangements"),
    ("Merritt v Merritt [1970] 1 WLR 1211", "contract law - intention to create legal relations", "residential property and family law"),

    # Contract - Misrepresentation
    ("Derry v Peek [1889] 14 App Cas 337", "contract law - misrepresentation", "financial services and investment"),

    # Contract - Frustration
    ("Davis Contractors Ltd v Fareham UDC [1956] AC 696", "contract law - frustration", "construction and public contracts"),
    ("Taylor v Caldwell [1863] 3 B&S 826", "contract law - frustration", "events and entertainment"),

    # Contract - Exclusion Clauses
    ("Photo Production Ltd v Securicor Transport Ltd [1980] AC 827", "contract law - exclusion clauses", "security and logistics"),
    ("L'Estrange v Graucob [1934] 2 KB 394", "contract law - exclusion clauses", "retail and consumer goods"),
    ("Thornton v Shoe Lane Parking [1971] 2 QB 163", "contract law - exclusion clauses", "transport and parking services"),

    # Contract - Remedies
    ("Hadley v Baxendale [1854] 9 Exch 341", "contract law - remedies for breach", "transport and logistics"),

    # Criminal Law
    ("R v Woollin [1999] 1 AC 82", "criminal law - mens rea and actus reus", "domestic and social care"),
    ("R v Cunningham [1957] 2 QB 396", "criminal law - mens rea and actus reus", "residential property"),
    ("R v Adomako [1995] 1 AC 171", "criminal law - murder and manslaughter", "healthcare and medical services"),
    ("R v Moloney [1985] AC 905", "criminal law - murder and manslaughter", "domestic and family"),
    ("R v Ghosh [1982] QB 1053", "criminal law - theft and fraud", "financial services and retail"),
    ("R v Hinks [2001] 2 AC 241", "criminal law - theft and fraud", "social care and elderly services"),
    ("R v Hasan [2005] UKHL 22", "criminal law - defences: duress", "organised crime and criminal law"),
    ("R v Sullivan [1984] AC 156", "criminal law - defences: insanity and automatism", "healthcare and criminal justice"),
    ("R v R [1992] 1 AC 599", "criminal law - assault and battery", "domestic and family law"),

    # Land Law
    ("Wheeldon v Burrows [1879] 12 Ch D 31", "land law - easements", "residential and rural property"),
    ("Re Ellenborough Park [1956] Ch 131", "land law - easements", "residential property development"),
    ("Tulk v Moxhay [1848] 2 Ph 774", "land law - covenants", "urban property and development"),
    ("Street v Mountford [1985] AC 809", "land law - leases and licences", "residential lettings and property"),
    ("Williams & Glyn's Bank v Boland [1981] AC 487", "land law - registration and overriding interests", "banking and residential property"),
    ("Thorner v Major [2009] UKHL 18", "land law - proprietary estoppel", "agriculture and rural property"),
    ("Pye v Graham [2002] UKHL 30", "land law - adverse possession", "agriculture and rural property"),

    # Equity and Trusts
    ("Westdeutsche Landesbank v Islington LBC [1996] AC 669", "equity and trusts - resulting trusts", "banking and local government"),
    ("Lloyds Bank v Rosset [1991] 1 AC 107", "equity and trusts - constructive trusts", "residential property and family law"),
    ("Keech v Sandford [1726] Sel Cas Ch 61", "equity and trusts - fiduciary duties", "estate and trust management"),
    ("Barnes v Addy [1874] LR 9 Ch App 244", "equity and trusts - breach of trust", "legal and financial services"),

    # Company Law
    ("Salomon v Salomon & Co Ltd [1897] AC 22", "company law - corporate personality", "manufacturing and small business"),
    ("Foss v Harbottle [1843] 2 Hare 461", "company law - shareholders rights", "corporate and investment"),
    ("Re Smith & Fawcett Ltd [1942] Ch 304", "company law - directors duties", "private limited companies"),
    ("Regal Hastings Ltd v Gulliver [1967] 2 AC 134", "company law - directors duties", "cinema and entertainment"),

    # Employment Law
    ("Ready Mixed Concrete v Minister of Pensions [1968] 2 QB 497", "employment law - employment status", "construction and logistics"),
    ("Western Excavating v Sharp [1978] QB 761", "employment law - unfair dismissal", "construction and contracting"),
    ("Polkey v AE Dayton Services Ltd [1988] AC 344", "employment law - unfair dismissal", "corporate and business services"),

    # Administrative Law
    ("Associated Provincial Picture Houses v Wednesbury Corporation [1948] 1 KB 223", "administrative law - judicial review", "local government and licensing"),
    ("Entick v Carrington [1765] 19 St Tr 1030", "constitutional law - rule of law", "government and public authority"),
    ("Factortame Ltd v Secretary of State [1990] 2 AC 85", "EU law - supremacy of EU law", "fishing and maritime industry"),

    # Intellectual Property
    ("Reckitt & Colman Products v Borden Inc [1990] 1 WLR 491", "intellectual property - passing off", "consumer goods and branding"),
    ("Designers Guild Ltd v Russell Williams [2000] 1 WLR 2416", "intellectual property - copyright infringement", "fashion and textile design"),

    # Consumer and Commercial Law
    ("Watteau v Fenwick [1893] 1 QB 346", "commercial law - agency", "hospitality and retail"),
]