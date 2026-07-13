import random
#create dictionary for Latin adjectives
latin_special_adj = {
    "Unus":["one"],
    "nUllus":["none","no"],
    "Ullus":["any"],
    "sOlus":["only","alone"],
    "neuter":["neither"],
    "alius":["another", "other"],
    "uter":["either"],
    "tOtus":["entire", "whole"],
    "alter":["the other"]
}

#randomize dictionary for iteration
list_of_lat_words = list(latin_special_adj.items())
random.shuffle(list_of_lat_words)
randomized_lat_adj_dic = dict(list_of_lat_words)

#latin declensions
first_declension = {
    "Puella": {
        "singular": {
            "Nominative":"puella",
            "Genitive":"puellae",
            "Dative":"puellae",
            "Accusative":"puellam",
            "Ablative":"puellA",
            "Vocative":"puella"
        },
        "plural" :{
            "Nominative":"puellae",
            "Genitive":"puellArum",
            "Dative":"puellIs",
            "Accusative":"puellAs",
            "Ablative":"puellIs",
            "Vocative":"puellae"
        }
    }
}

second_declension = {
    "AmIcus": {
        "singular": {
            "Nominative":"amIcus",
            "Genitive":"amIcI",
            "Dative":"amIcO",
            "Accusative":"amIcum",
            "Ablative":"amIcO",
            "Vocative":"amIce"
        },
        "plural" :{
            "Nominative":"amIcI",
            "Genitive":"amIcOrum",
            "Dative":"amIcIs",
            "Accusative":"amIcOs",
            "Ablative":"amIcIs",
            "Vocative":"amIcI"
        }
    }
}

second_declension_neuter = {
    "Bellum": {
        "singular": {
            "Nominative":"bellum",
            "Genitive":"bellI",
            "Dative":"bellO",
            "Accusative":"bellum",
            "Ablative":"bellO",
            "Vocative":"bellum"
        },
        "plural" :{
            "Nominative":"bella",
            "Genitive":"bellOrum",
            "Dative":"bellIs",
            "Accusative":"bella",
            "Ablative":"bellIs",
            "Vocative":"bella"
        }
    }
}

third_declension = {
    "REx": {
        "singular": {
            "Nominative":"rEx",
            "Genitive":"rEgis",
            "Dative":"rEgI",
            "Accusative":"rEgem",
            "Ablative":"rEge",
            "Vocative":"rEx"
        },
        "plural" :{
            "Nominative":"rEgEs",
            "Genitive":"rEgum",
            "Dative":"rEgibus",
            "Accusative":"rEgEs",
            "Ablative":"rEgibus",
            "Vocative":"rEgEs"
        }
    },
    "VirtUs": {
        "singular": {
            "Nominative":"virtUs",
            "Genitive":"virtUtis",
            "Dative":"virtUtI",
            "Accusative":"virtUtem",
            "Ablative":"virtUte",
            "Vocative":"virtUs"
        },
        "plural" :{
            "Nominative":"virtUtEs",
            "Genitive":"virtUtum",
            "Dative":"virtUtibus",
            "Accusative":"virtUtEs",
            "Ablative":"virtUtibus",
            "Vocative":"virtUtEs"
        }
    },
        "Corpus": {
        "singular": {
            "Nominative":"corpus",
            "Genitive":"corporis",
            "Dative":"corpI",
            "Accusative":"corpus",
            "Ablative":"corpore",
            "Vocative":"corpus"
        },
        "plural" :{
            "Nominative":"corpora",
            "Genitive":"corporur",
            "Dative":"corporibus",
            "Accusative":"corpora",
            "Ablative":"corporibus",
            "Vocative":"corpora"
        
        }
    }
}
