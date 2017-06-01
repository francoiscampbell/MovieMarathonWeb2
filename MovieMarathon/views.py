from django.http import HttpResponse
from django.shortcuts import render

import requests
import requests_mock

from . import secrets


# Create your views here.
def index(request):
    context = {
        'PLACES_API_KEY': secrets.PLACES_API_KEY
    }
    return render(request, 'index.html', context)


def movies(request):
    params = request.GET.copy()
    params['api_key'] = secrets.TMS_API_KEY
    with requests_mock.mock() as m:
        m.get('http://data.tmsapi.com/v1.1/movies/showings', text=mock_text)
        response = requests.get('http://data.tmsapi.com/v1.1/movies/showings', params=params)
        return HttpResponse(response.text)

mock_text = r"""
[{
    "tmsId": "MV009512900000",
    "rootId": "13506541",
    "subType": "Feature Film",
    "title": "Citizen Jane: Battle for the City",
    "releaseYear": 2016,
    "releaseDate": "2016-09-09",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "Arguably no one did more to shape understanding of the modern American city than Jane Jacobs, the visionary activist and author of \"The Death and Life of Great American Cities\" who fought to preserve urban communities in the face of destructive development projects. Here, she fights against the ruthless redevelopment projects of urban planner Robert Moses.",
    "shortDescription": "Writer and urban activist Jane Jacobs fights to save historic New York City during the 1960s.",
    "directors": ["Matt Tyrnauer"],
    "officialUrl": "http://www.altimeterfilms.com/citizen-jane-battle-for-the-city",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "runTime": "PT01H32M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13506541_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "6030",
            "name": "Hot Docs Ted Rogers Cinema"
        },
        "dateTime": "2017-05-27T18:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T16:10",
        "barg": false
    }]
}, {
    "tmsId": "EV000005156329",
    "rootId": "11256785",
    "subType": "Theatre Event",
    "title": "Hump Film Festival",
    "titleLang": "en",
    "entityType": "Movie",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "6030",
            "name": "Hot Docs Ted Rogers Cinema"
        },
        "dateTime": "2017-05-27T21:00",
        "barg": false
    }]
}, {
    "tmsId": "MV007898160000",
    "rootId": "12009531",
    "subType": "Feature Film",
    "title": "Pirates of the Caribbean: Dead Men Tell No Tales",
    "releaseYear": 2017,
    "releaseDate": "2017-05-26",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Action", "Fantasy"],
    "longDescription": "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy.",
    "shortDescription": "Deadly ghost sailors pursue Jack Sparrow as he searches for the legendary Trident of Poseidon.",
    "topCast": ["Johnny Depp", "Geoffrey Rush", "Javier Bardem"],
    "directors": ["Joachim Rønning", "Espen Sandberg"],
    "officialUrl": "http://pirates.disney.com/pirates-of-the-caribbean-dead-men-tell-no-tales",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT02H09M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Pirates of the Caribbean: Dead Men Tell No Tales -- The IMAX 2D Experience (2017)",
            "lang": "en"
        },
        "uri": "assets/p12009531_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T10:30",
        "quals": "Closed Captioned|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "Closed Captioned|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T11:30",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T14:30",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T17:30",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T20:30",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T23:30",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T12:50",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T15:50",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T21:40",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T12:15",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T15:15",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T21:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T15:40",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T21:50",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV009714670000",
    "rootId": "13690994",
    "subType": "Feature Film",
    "title": "Paris Can Wait",
    "releaseYear": 2016,
    "releaseDate": "2016-09-12",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Romantic comedy"],
    "longDescription": "Anne (Diane Lane) is at a crossroads in her life. Married to a successful but inattentive movie producer (Alec Baldwin), she unexpectedly finds herself taking a car trip from Cannes to Paris with her husband's business associate (Arnaud Viard). What should be a seven-hour drive turns into a carefree two-day adventure replete with diversions involving picturesque sights, fine food and wine, humor, wisdom and romance, reawakening Anne's senses and giving her a new lust for life.",
    "shortDescription": "A woman must fend off advances from her husband's colleague while taking a road trip through France.",
    "topCast": ["Diane Lane", "Arnaud Viard", "Alec Baldwin"],
    "directors": ["Eleanor Coppola"],
    "officialUrl": "http://sonyclassics.com/pariscanwait/#",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H32M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Paris Can Wait (2016)",
            "lang": "en"
        },
        "uri": "assets/p13690994_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T10:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T14:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T17:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T18:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T19:35",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T21:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T21:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009295130000",
    "rootId": "13259824",
    "subType": "Feature Film",
    "title": "I, Daniel Blake",
    "releaseYear": 2016,
    "releaseDate": "2016-05-12",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Drama"],
    "longDescription": "Daniel Blake (Dave Johns) is a 59-year-old widowed carpenter who must rely on welfare after a recent heart attack leaves him unable to work. Despite his doctor's diagnosis, British authorities deny Blake's benefits and tell him to return to his job. As Daniel navigates his way through an agonizing appeal process, he begins to develop a strong bond with a destitute, single mother (Hayley Squires) who's struggling to take care of her two children.",
    "shortDescription": "A British widower befriends a destitute, single mother while fighting to keep his welfare benefits.",
    "topCast": ["Dave Johns", "Hayley Squires", "Dylan McKiernan"],
    "directors": ["Ken Loach"],
    "officialUrl": "http://www.ifcfilms.com/films/i-daniel-blake",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H40M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13259824_v_v5_az.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T10:30",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:15",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T14:45",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T17:10",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T19:40",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T22:10",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T11:15",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T13:40",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T16:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T18:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T21:15",
        "barg": false
    }]
}, {
    "tmsId": "MV009294920000",
    "rootId": "13259663",
    "subType": "Feature Film",
    "title": "Alone in Berlin",
    "releaseYear": 2016,
    "releaseDate": "2016-02-15",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Historical drama"],
    "longDescription": "The mission is the message.",
    "shortDescription": "A German couple lose their son in WWII, prompting them to become secretly anti-Nazi.",
    "topCast": ["Emma Thompson", "Brendan Gleeson", "Daniel Brühl"],
    "directors": ["Vincent Perez"],
    "officialUrl": "http://www.ifcfilms.com/films/alone-in-berlin",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT01H43M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13259663_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T10:30",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:55",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:35",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T21:25",
        "barg": false
    }]
}, {
    "tmsId": "MV009659840000",
    "rootId": "13612977",
    "subType": "Feature Film",
    "title": "Snatched",
    "releaseYear": 2017,
    "releaseDate": "2017-05-12",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Action", "Comedy", "Adventure"],
    "longDescription": "Dumped by her boyfriend on the eve of their vacation, impetuous dreamer Emily Middleton persuades her cautious mother, Linda, to accompany her on an exotic getaway to South America. Polar opposites, Emily and Linda must soon work through their differences to escape from a wildly outrageous and dangerous jungle adventure.",
    "shortDescription": "A woman and her mother become the target of kidnappers while on vacation in South America.",
    "topCast": ["Amy Schumer", "Goldie Hawn", "Wanda Sykes"],
    "directors": ["Jonathan Levine"],
    "officialUrl": "http://www.foxmovies.com/movies/snatched",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Brief Nudity"],
    "runTime": "PT01H30M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13612977_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T10:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T17:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T20:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T22:25",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T14:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T17:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T20:20",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T11:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T15:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T18:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T20:25",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T19:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T22:15",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009302840000",
    "rootId": "13267188",
    "subType": "Feature Film",
    "title": "Maudie",
    "releaseYear": 2016,
    "releaseDate": "2016-09-02",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Biography", "Romance", "Historical drama"],
    "longDescription": "Canadian folk artist Maud Lewis (Sally Hawkins) falls in love with a fishmonger (Ethan Hawke) while working for him as a live-in housekeeper.",
    "shortDescription": "Folk artist Maud Lewis falls in love with a fishmonger while working for him as a housekeeper.",
    "topCast": ["Sally Hawkins", "Ethan Hawke", "Kari Matchett"],
    "directors": ["Aisling Walsh"],
    "officialUrl": "http://sonyclassics.com/maudie/",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT01H55M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Maudie (2016)",
            "lang": "en"
        },
        "uri": "assets/p13267188_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:15",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:45",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T18:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T18:10",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T21:00",
        "quals": "VIP 19+|Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T21:00",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "5345",
            "name": "The Revue Cinema"
        },
        "dateTime": "2017-05-27T16:00",
        "barg": false
    }, {
        "theatre": {
            "id": "5345",
            "name": "The Revue Cinema"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T12:50",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:10",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T20:55",
        "quals": "Closed Captioned",
        "barg": false
    }]
}, {
    "tmsId": "MV007787080000",
    "rootId": "11714883",
    "subType": "Feature Film",
    "title": "Guardians of the Galaxy Vol. 2 3D",
    "releaseYear": 2017,
    "releaseDate": "2017-05-05",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Science fiction", "Adventure", "Action", "Fantasy", "Comedy"],
    "longDescription": "Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that Rocket has stolen the items they were sent to guard, the Sovereign dispatch their armada to search for vengeance. As the Guardians try to escape, the mystery of Peter's parentage is revealed.",
    "shortDescription": "The team unravels the mystery of Peter Quill's true parentage in the outer reaches of the galaxy.",
    "topCast": ["Chris Pratt", "Zoe Saldana", "Bradley Cooper"],
    "directors": ["James Gunn"],
    "officialUrl": "http://movies.disney.com/guardians-of-the-galaxy-vol-2",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT02H15M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Guardians of the Galaxy Vol. 2 3D (2017)",
            "lang": "en"
        },
        "uri": "assets/p11714883_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:30",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T13:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T16:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T22:15",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T22:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T12:45",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:30",
        "quals": "UltraAVX",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T15:50",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:30",
        "quals": "UltraAVX",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "UltraAVX",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:00",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:35",
        "quals": "UltraAVX",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T20:20",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T23:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:30",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T16:30",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:30",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T12:15",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T21:50",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T12:45",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:10",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:20",
        "quals": "CC/DVS",
        "barg": false
    }]
}, {
    "tmsId": "MV007898170000",
    "rootId": "12009531",
    "subType": "Feature Film",
    "title": "Pirates of the Caribbean: Dead Men Tell No Tales 3D",
    "releaseYear": 2017,
    "releaseDate": "2017-05-26",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Action", "Fantasy"],
    "longDescription": "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy.",
    "shortDescription": "Deadly ghost sailors pursue Jack Sparrow as he searches for the legendary Trident of Poseidon.",
    "topCast": ["Johnny Depp", "Geoffrey Rush", "Javier Bardem"],
    "directors": ["Joachim Rønning", "Espen Sandberg"],
    "officialUrl": "http://pirates.disney.com/pirates-of-the-caribbean-dead-men-tell-no-tales",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT02H09M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Pirates of the Caribbean: Dead Men Tell No Tales -- The IMAX 2D Experience (2017)",
            "lang": "en"
        },
        "uri": "assets/p12009531_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:40",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T12:50",
        "quals": "Closed Captioned|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T19:10",
        "quals": "Closed Captioned|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T22:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T22:20",
        "quals": "Closed Captioned|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T11:00",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:50",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T14:00",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:55",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T17:00",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "No Passes|UltraAVX|VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T20:00",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:05",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T23:00",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T12:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:20",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T15:45",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T16:25",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:35",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:15",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:40",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T12:45",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T22:00",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T12:30",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T13:20",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T16:20",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T18:45",
        "quals": "CC/DVS|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:35",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV009709390000",
    "rootId": "13682500",
    "subType": "Feature Film",
    "title": "The Lovers",
    "releaseYear": 2017,
    "releaseDate": "2017-04-22",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Romantic comedy"],
    "longDescription": "A man and his wife, each embroiled in an extramarital affair, are sent reeling when they suddenly fall for the least likely person imaginable -- each other.",
    "shortDescription": "Two cheating spouses suddenly fall for the least likely person imaginable -- each other.",
    "topCast": ["Debra Winger", "Tracy Letts", "Melora Walters"],
    "directors": ["Azazel Jacobs"],
    "officialUrl": "http://a24films.com/films/the-lovers/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H34M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Lovers (2017)",
            "lang": "en"
        },
        "uri": "assets/p13682500_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T13:20",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:55",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T18:40",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T21:20",
        "quals": "Closed Captioned",
        "barg": false
    }]
}, {
    "tmsId": "MV007508410000",
    "rootId": "11714883",
    "subType": "Feature Film",
    "title": "Guardians of the Galaxy Vol. 2",
    "releaseYear": 2017,
    "releaseDate": "2017-05-05",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Science fiction", "Adventure", "Action", "Fantasy", "Comedy"],
    "longDescription": "Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that Rocket has stolen the items they were sent to guard, the Sovereign dispatch their armada to search for vengeance. As the Guardians try to escape, the mystery of Peter's parentage is revealed.",
    "shortDescription": "The team unravels the mystery of Peter Quill's true parentage in the outer reaches of the galaxy.",
    "topCast": ["Chris Pratt", "Zoe Saldana", "Bradley Cooper"],
    "directors": ["James Gunn"],
    "officialUrl": "http://movies.disney.com/guardians-of-the-galaxy-vol-2",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT02H15M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p11714883_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "9035",
            "name": "Cineplex Cinemas Varsity and VIP"
        },
        "dateTime": "2017-05-27T15:40",
        "quals": "Closed Captioned",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T14:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T17:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T20:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T17:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T12:45",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T15:45",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T21:45",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T12:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T15:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T12:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T15:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T18:55",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T21:45",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T15:40",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T15:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV008740810000",
    "rootId": "12740508",
    "subType": "Feature Film",
    "title": "The LEGO Batman Movie",
    "releaseYear": 2017,
    "releaseDate": "2017-02-10",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Adventure", "Action", "Animated", "Children"],
    "audience": "Children",
    "longDescription": "There are big changes brewing in Gotham, but if Batman (Will Arnett) wants to save the city from the Joker's (Zach Galifianakis) hostile takeover, he may have to drop the lone vigilante thing, try to work with others and maybe, just maybe, learn to lighten up. Maybe his superhero sidekick Robin (Michael Cera) and loyal butler Alfred (Ralph Fiennes) can show him a thing or two.",
    "shortDescription": "Batman (Will Arnett) must save Gotham City from the Joker's (Zach Galifianakis) hostile takeover.",
    "topCast": ["Will Arnett", "Michael Cera", "Rosario Dawson"],
    "directors": ["Chris McKay"],
    "officialUrl": "http://www.legobatman.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H46M",
    "animation": "Animated",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12740508_v_v5_ab.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "2660",
            "name": "The Royal"
        },
        "dateTime": "2017-05-27T14:00",
        "barg": false
    }]
}, {
    "tmsId": "MV009877390000",
    "rootId": "13910117",
    "subType": "Feature Film",
    "title": "The Transfiguration",
    "releaseYear": 2016,
    "releaseDate": "2016-05-14",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Horror", "Thriller"],
    "longDescription": "Troubled teen Milo (Eric Ruffin) hides behind his fascination with vampire lore. When he meets the equally alienated Sophie (Chloe Levine), the two form a bond that begins to challenge Milo's dark obsession, blurring his fantasy into reality.",
    "shortDescription": "Fascinated with vampire lore, a troubled teen forms a bond with an equally alienated girl.",
    "topCast": ["Eric Ruffin", "Chloe Levine", "Aaron Clifton Moten"],
    "directors": ["Michael O'Shea"],
    "officialUrl": "http://www.thetransfigurationfilm.com/",
    "advisories": ["Adult Language", "Adult Situations", "Graphic Violence"],
    "runTime": "PT01H37M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Transfiguration (2016)",
            "lang": "en"
        },
        "uri": "assets/p13910117_p_v5_ac.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "2660",
            "name": "The Royal"
        },
        "dateTime": "2017-05-27T16:30",
        "barg": false
    }]
}, {
    "tmsId": "MV009341300000",
    "rootId": "13307887",
    "subType": "Feature Film",
    "title": "The Northlander",
    "releaseYear": 2016,
    "releaseDate": "2016",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Action", "Adventure", "Fantasy", "Science fiction"],
    "longDescription": "In the year 2961, a hunter in one of the last surviving human bands travels across a dangerous land to save his people.",
    "shortDescription": "A hunter from one of the last human bands travels across a dangerous land to save his people.",
    "topCast": ["Corey Sevier", "Roseanne Supernault", "Michelle Thrush"],
    "directors": ["Benjamin Ross Hayden"],
    "runTime": "PT01H38M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "2660",
            "name": "The Royal"
        },
        "dateTime": "2017-05-27T19:00",
        "barg": false
    }]
}, {
    "tmsId": "MV009324070000",
    "rootId": "13292723",
    "subType": "Feature Film",
    "title": "Personal Shopper",
    "releaseYear": 2016,
    "releaseDate": "2016-05-16",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Thriller", "Mystery", "Drama"],
    "longDescription": "A young American in Paris works as a personal shopper for a celebrity. She seems to have the ability to communicate with spirits, like her recently deceased twin brother. Soon, she starts to receive ambiguous messages from an unknown source.",
    "shortDescription": "A young American woman in Paris starts to receive ambiguous messages from an unknown source.",
    "topCast": ["Kristen Stewart", "Lars Eidinger", "Sigrid Bouaziz"],
    "directors": ["Olivier Assayas"],
    "officialUrl": "http://www.ifcfilms.com/films/personal-shopper",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Nudity", "Violence"],
    "runTime": "PT01H45M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13292723_v_v5_ak.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "2660",
            "name": "The Royal"
        },
        "dateTime": "2017-05-27T21:30",
        "barg": false
    }]
}, {
    "tmsId": "MV008331720000",
    "rootId": "12394972",
    "subType": "Feature Film",
    "title": "King Arthur: Legend of the Sword",
    "releaseYear": 2017,
    "releaseDate": "2017-05-12",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Action", "Fantasy"],
    "longDescription": "After the murder of his father, young Arthur's power-hungry uncle Vortigern seizes control of the crown. Robbed of his birthright, he grows up the hard way in the back alleys of the city, not knowing who he truly is. When fate leads him to pull the Excalibur sword from stone, Arthur embraces his true destiny to become a legendary fighter and leader.",
    "shortDescription": "Robbed of his birthright, Arthur embraces his destiny after pulling the Excalibur sword from stone.",
    "topCast": ["Charlie Hunnam", "Astrid Bergès-Frisbey", "Jude Law"],
    "directors": ["Guy Ritchie"],
    "officialUrl": "http://kingarthurmovie.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT02H06M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "King Arthur: Legend of the Sword (2017)",
            "lang": "en"
        },
        "uri": "assets/p12394972_p_v5_ag.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:15",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T15:55",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:40",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:20",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T12:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T15:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T18:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T21:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T11:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T14:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:00",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:30",
        "quals": "VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T12:40",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T15:40",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T18:50",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T21:50",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T16:20",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T12:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T15:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T18:35",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T21:15",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T15:30",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T16:10",
        "barg": false
    }]
}, {
    "tmsId": "MV007343300000",
    "rootId": "11606343",
    "subType": "Feature Film",
    "title": "Beauty and the Beast",
    "releaseYear": 2017,
    "releaseDate": "2017-03-17",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Musical", "Fantasy", "Romance"],
    "longDescription": "Belle (Emma Watson), a bright, beautiful and independent young woman, is taken prisoner by a beast (Dan Stevens) in its castle. Despite her fears, she befriends the castle's enchanted staff and learns to look beyond the beast's hideous exterior, allowing her to recognize the kind heart and soul of the true prince that hides on the inside.",
    "shortDescription": "A young woman discovers the kind heart and soul of a beast who keeps her in its castle.",
    "topCast": ["Emma Watson", "Dan Stevens", "Luke Evans"],
    "directors": ["Bill Condon"],
    "officialUrl": "http://movies.disney.com/beauty-and-the-beast-2017",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT02H09M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p11606343_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:15",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T15:55",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:35",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T13:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009445370000",
    "rootId": "13425972",
    "subType": "Feature Film",
    "title": "Their Finest",
    "releaseYear": 2016,
    "releaseDate": "2016-09-11",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Romantic comedy", "Historical drama"],
    "longDescription": "In 1940, a married woman (Gemma Arterton) and a screenwriter (Sam Claflin) develop a growing attraction while working together on a propaganda film about the evacuation of Allied troops from Dunkirk, France.",
    "shortDescription": "In 1940, two writers develop a growing attraction while working together on a propaganda film.",
    "topCast": ["Gemma Arterton", "Sam Claflin", "Bill Nighy"],
    "directors": ["Lone Scherfig"],
    "officialUrl": "http://www.stxmovies.com/theirfinest/#about",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H57M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13425972_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T21:15",
        "barg": false
    }]
}, {
    "tmsId": "MV008260190000",
    "rootId": "12343481",
    "subType": "Feature Film",
    "title": "Alien: Covenant",
    "releaseYear": 2017,
    "releaseDate": "2017-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Science fiction", "Horror", "Thriller"],
    "longDescription": "Bound for a remote planet on the far side of the galaxy, members (Katherine Waterston, Billy Crudup) of the colony ship Covenant discover what they think to be an uncharted paradise. While there, they meet David (Michael Fassbender), the synthetic survivor of the doomed Prometheus expedition. The mysterious world soon turns dark and dangerous when a hostile alien life-form forces the crew into a deadly fight for survival.",
    "shortDescription": "Crew members of a colony ship encounter a hostile alien life-form on a dark and dangerous planet.",
    "topCast": ["Michael Fassbender", "Katherine Waterston", "Billy Crudup"],
    "directors": ["Ridley Scott"],
    "officialUrl": "http://www.foxmovies.com/movies/alien-covenant",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Graphic Violence", "Nudity"],
    "runTime": "PT02H02M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12343481_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T15:55",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:40",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:25",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:15",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:10",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:05",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:05",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T11:45",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T12:55",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T16:00",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T19:00",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T22:00",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T12:10",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:15",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T15:20",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T16:20",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T18:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:20",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T21:45",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:20",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T12:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T15:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T19:05",
        "barg": false
    }, {
        "theatre": {
            "id": "10297",
            "name": "Humber Cinemas"
        },
        "dateTime": "2017-05-27T21:55",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T16:10",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T19:10",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T22:10",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:00",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:00",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV009848120000",
    "rootId": "13872116",
    "subType": "Feature Film",
    "title": "Population Zero",
    "releaseYear": 2016,
    "releaseDate": "2016",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Crime drama", "Mystery", "Thriller"],
    "shortDescription": "In 2009, three young men are killed in Yellowstone National Park.",
    "longDescription": "In 2009, three young men are killed in Yellowstone National Park.",
    "topCast": ["Julian T. Pinder"],
    "directors": ["Julian T. Pinder", "Adam Levins"],
    "runTime": "PT01H24M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13872116_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }]
}, {
    "tmsId": "MV008858190000",
    "rootId": "12840441",
    "subType": "Feature Film",
    "title": "Baywatch",
    "releaseYear": 2017,
    "releaseDate": "2017-05-25",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Action"],
    "longDescription": "Matt Brody is a former Olympic swimmer who wants to join an elite team of lifeguards led by the hulking Mitch Buchannon. Brody thinks he's a shoo-in, but his casual attitude starts to instantly rub Mitch the wrong way. When drugs and a shady resort owner pose a threat to the bay, Mitch and Matt must put their differences aside to spring into action and save the day.",
    "shortDescription": "A hulking lifeguard and a new recruit spring into action to save their bay from drugs and criminals.",
    "topCast": ["Dwayne Johnson", "Zac Efron", "Priyanka Chopra"],
    "directors": ["Seth Gordon"],
    "officialUrl": "http://www.baywatchfilm.com/",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Nudity"],
    "runTime": "PT01H59M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Baywatch (2017)",
            "lang": "en"
        },
        "uri": "assets/p12840441_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T16:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:25",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T12:50",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:40",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T15:35",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:40",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T18:45",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:45",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T21:40",
        "quals": "Closed Caption & Descriptive Video|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:45",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T16:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:50",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T23:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T13:00",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T15:55",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T18:55",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T21:55",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:40",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T16:15",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T16:40",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:45",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:45",
        "quals": "No Passes|VIP 19+",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:45",
        "quals": "VIP 19+|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T13:15",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T16:20",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T19:20",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T22:20",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T13:50",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T16:50",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:45",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:45",
        "quals": "UltraAVX|No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV009512940000",
    "rootId": "13506592",
    "subType": "Feature Film",
    "title": "Everything, Everything",
    "releaseYear": 2017,
    "releaseDate": "2017-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Drama", "Romance"],
    "longDescription": "Maddy (Amandla Stenberg) is a smart, curious and imaginative 18-year-old who is unable to leave the protection of the hermetically-sealed environment within her house because of an illness. Olly (Nick Robinson) is the boy next door who won't let that stop them from being together. Gazing through windows and talking only through texts, Maddy and Olly form a deep bond that leads them to risk everything to be together, even if it means losing everything.",
    "shortDescription": "A sick 18-year-old who can't leave the house develops a budding romance with her new neighbor.",
    "topCast": ["Amandla Stenberg", "Nick Robinson", "Anika Noni Rose"],
    "directors": ["Stella Meghie"],
    "officialUrl": "http://everythingeverythingmovie.com/",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H36M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Everything, Everything (2017)",
            "lang": "en"
        },
        "uri": "assets/p13506592_p_v5_ac.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T15:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:55",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:10",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T11:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T14:25",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T17:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:20",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T13:05",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T16:05",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T19:05",
        "barg": false
    }, {
        "theatre": {
            "id": "6738",
            "name": "Rainbow Cinemas Market Square"
        },
        "dateTime": "2017-05-27T22:05",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T11:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T15:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T18:05",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T20:25",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T12:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T14:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T17:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009213130000",
    "rootId": "13174411",
    "subType": "Feature Film",
    "title": "Diary of a Wimpy Kid: The Long Haul",
    "releaseYear": 2017,
    "releaseDate": "2017-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Adventure", "Children"],
    "audience": "Children",
    "longDescription": "Young Greg Heffley is looking forward to a long summer of just hanging out, but his mother throws a monkey wrench into his plans when she forces the entire family to take a road trip for a relative's birthday celebration. His eyes soon light up after he realizes that the excursion is his ticket to a gaming convention to meet YouTube sensation Mac Digby. Greg's imagination then kicks into overdrive as he sneakily hatches a scheme to attend the expo and gain some much-deserved fame.",
    "shortDescription": "A family road trip takes a wrong turn when a boy hatches a scheme to attend a gaming convention.",
    "topCast": ["Jason Drucker", "Alicia Silverstone", "Tom Everett Scott"],
    "directors": ["David Bowers"],
    "officialUrl": "http://www.foxmovies.com/movies/diary-of-a-wimpy-kid-the-long-haul",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H31M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13174411_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T13:35",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T16:15",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T19:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T14:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T17:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T11:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:05",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T15:20",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T17:35",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T11:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T14:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T16:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T18:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T21:20",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009856690000",
    "rootId": "13689689",
    "subType": "Feature Film",
    "title": "Norman",
    "releaseYear": 2016,
    "releaseDate": "2016-09-03",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy drama"],
    "longDescription": "Norman (Richard Gere), a New York fixer, knows the right people and can get things done. When an Israeli dignitary named Eshel (Lior Ashkenazi) comes to the city, Norman decides to impress the man by buying him some very expensive shoes. It works and he establishes a strong connection to the man, but a few years later, when Eshel becomes the Israel prime minister, Norman can't communicate with him anymore, and this threatens to destroy his reputation.",
    "shortDescription": "A financial schemer (Richard Gere) finds himself in the middle of an international scandal.",
    "topCast": ["Richard Gere", "Lior Ashkenazi", "Michael Sheen"],
    "directors": ["Joseph Cedar"],
    "officialUrl": "http://sonyclassics.com/norman/#",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H58M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13689689_i_v5_aa.jpg",
        "category": "Iconic",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T15:50",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:05",
        "barg": false
    }]
}, {
    "tmsId": "MV009322060000",
    "rootId": "13290196",
    "subType": "Feature Film",
    "title": "Colossal",
    "releaseYear": 2016,
    "releaseDate": "2016-09-09",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Fantasy"],
    "longDescription": "Gloria (Anne Hathaway) drinks too hard and parties too much. Her boyfriend has enough of it and throws her out. Gloria returns to her hometown, dreaming of making a new start, but instead revives her childhood friendship with Oscar (Jason Sudeikis), who runs a bar. After drinking a night away with Oscar and his friends, he wakes up to discover a gigantic monster rampaging through Seoul and realizes that somehow the monster is connected to her.",
    "shortDescription": "Oscar discovers a connection between his childhood friend and a rampaging monster.",
    "topCast": ["Anne Hathaway", "Jason Sudeikis", "Austin Stowell"],
    "directors": ["Nacho Vigalondo"],
    "officialUrl": "http://sheiscolossal.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT01H50M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Colossal (2016)",
            "lang": "en"
        },
        "uri": "assets/p13290196_p_v5_ab.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T16:05",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:00",
        "barg": false
    }]
}, {
    "tmsId": "MV009395580000",
    "rootId": "13365032",
    "subType": "Feature Film",
    "title": "Get Out",
    "releaseYear": 2017,
    "releaseDate": "2017-01-24",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Horror"],
    "longDescription": "Now that Chris (Daniel Kaluuya) and his girlfriend, Rose (Allison Williams), have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean. At first, Chris reads the family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined.",
    "shortDescription": "A young man uncovers a dark secret when he meets his girlfriend's parents for the first time.",
    "topCast": ["Daniel Kaluuya", "Allison Williams", "Catherine Keener"],
    "directors": ["Jordan Peele"],
    "officialUrl": "http://www.getoutfilm.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Graphic Violence"],
    "runTime": "PT01H44M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13365032_v_v5_ad.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T18:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T21:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T20:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T23:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV001381460000",
    "rootId": "81732",
    "subType": "Feature Film",
    "title": "The Room",
    "releaseYear": 2003,
    "releaseDate": "2003-06-27",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Drama"],
    "longDescription": "A successful banker's (Tommy Wiseau) fiancee (Juliette Danielle) tempts and manipulates his best friend (Greg Sestero).",
    "shortDescription": "A banker's (Tommy Wiseau) fiancee (Juliette Danielle) manipulates his best friend (Greg Sestero).",
    "topCast": ["Tommy Wiseau", "Juliette Danielle", "Greg Sestero"],
    "directors": ["Tommy Wiseau"],
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "1"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Nudity", "Violence"],
    "runTime": "PT01H39M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p81732_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10257",
            "name": "Carlton Cinema"
        },
        "dateTime": "2017-05-27T23:00",
        "barg": false
    }]
}, {
    "tmsId": "MV007534630000",
    "rootId": "11730466",
    "subType": "Feature Film",
    "title": "The Fate of the Furious",
    "releaseYear": 2017,
    "releaseDate": "2017-04-14",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Action", "Adventure", "Thriller"],
    "longDescription": "With Dom and Letty married, Brian and Mia retired and the rest of the crew exonerated, the globe-trotting team has found some semblance of a normal life. They soon face an unexpected challenge when a mysterious woman named Cipher forces Dom to betray them all. Now, they must unite to bring home the man who made them a family and stop Cipher from unleashing chaos.",
    "shortDescription": "Members of the crew spring into action when a mysterious woman forces Dom to betray them all.",
    "topCast": ["Vin Diesel", "Dwayne Johnson", "Charlize Theron"],
    "directors": ["F. Gary Gray"],
    "officialUrl": "http://www.fastandfurious.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT02H16M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Fate of the Furious (2017)",
            "lang": "en"
        },
        "uri": "assets/p11730466_p_v5_ae.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T12:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T15:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T18:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T21:55",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T12:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T18:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T21:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009428660000",
    "rootId": "13407523",
    "subType": "Feature Film",
    "title": "The Lost City of Z",
    "releaseYear": 2016,
    "releaseDate": "2016-10-14",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Historical drama", "Biography"],
    "longDescription": "At the dawn of the 20th century, British explorer Percy Fawcett journeys into the Amazon, where he discovers evidence of a previously unknown, advanced civilization that may have once inhabited the region. Despite being ridiculed by the scientific establishment, which views indigenous populations as savages, the determined Fawcett, supported by his devoted wife, son, and aide-de-camp, returns to his beloved jungle in an attempt to prove his case.",
    "shortDescription": "British explorer Col. Percival Fawcett ventures into Amazon at the dawn of the 20th century.",
    "topCast": ["Charlie Hunnam", "Robert Pattinson", "Sienna Miller"],
    "directors": ["James Gray"],
    "officialUrl": "http://www.bleeckerstreetmedia.com/thelostcityofz",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Nudity", "Violence"],
    "runTime": "PT02H21M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Lost City of Z (2016)",
            "lang": "en"
        },
        "uri": "assets/p13407523_p_v5_ac.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:00",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:05",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:10",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:15",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T12:55",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T15:50",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T17:55",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T20:50",
        "barg": false
    }]
}, {
    "tmsId": "MV007343310000",
    "rootId": "11606343",
    "subType": "Feature Film",
    "title": "Beauty and the Beast 3D",
    "releaseYear": 2017,
    "releaseDate": "2017-03-17",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Musical", "Fantasy", "Romance"],
    "longDescription": "Belle (Emma Watson), a bright, beautiful and independent young woman, is taken prisoner by a beast (Dan Stevens) in its castle. Despite her fears, she befriends the castle's enchanted staff and learns to look beyond the beast's hideous exterior, allowing her to recognize the kind heart and soul of the true prince that hides on the inside.",
    "shortDescription": "A young woman discovers the kind heart and soul of a beast who keeps her in its castle.",
    "topCast": ["Emma Watson", "Dan Stevens", "Luke Evans"],
    "directors": ["Bill Condon"],
    "officialUrl": "http://movies.disney.com/beauty-and-the-beast-2017",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT02H09M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Beauty and the Beast 3D (2017)",
            "lang": "en"
        },
        "uri": "assets/p11606343_p_v5_ah.jpg",
        "category": "Poster Art",
        "text": "yes"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:05",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T18:55",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T21:50",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:40",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:50",
        "quals": "CC/DVS",
        "barg": false
    }]
}, {
    "tmsId": "MV008800750000",
    "rootId": "12792395",
    "subType": "Feature Film",
    "title": "Logan",
    "releaseYear": 2017,
    "releaseDate": "2017-02-16",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Action", "Adventure"],
    "longDescription": "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border. His plan to hide from the outside world gets upended when he meets a young mutant (Dafne Keen) who is very much like him. Logan must now protect the girl and battle the dark forces that want to capture her.",
    "shortDescription": "A weary Logan cares for an ailing Professor X while protecting a young mutant girl from dark forces.",
    "topCast": ["Hugh Jackman", "Patrick Stewart", "Dafne Keen"],
    "directors": ["James Mangold"],
    "officialUrl": "http://www.foxmovies.com/movies/logan",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Brief Nudity", "Graphic Violence"],
    "runTime": "PT02H15M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12792395_v_v5_al.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:25",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV008331780000",
    "rootId": "12394972",
    "subType": "Feature Film",
    "title": "King Arthur: Legend of the Sword 3D",
    "releaseYear": 2017,
    "releaseDate": "2017-05-12",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Action", "Fantasy"],
    "longDescription": "After the murder of his father, young Arthur's power-hungry uncle Vortigern seizes control of the crown. Robbed of his birthright, he grows up the hard way in the back alleys of the city, not knowing who he truly is. When fate leads him to pull the Excalibur sword from stone, Arthur embraces his true destiny to become a legendary fighter and leader.",
    "shortDescription": "Robbed of his birthright, Arthur embraces his destiny after pulling the Excalibur sword from stone.",
    "topCast": ["Charlie Hunnam", "Astrid Bergès-Frisbey", "Jude Law"],
    "directors": ["Guy Ritchie"],
    "officialUrl": "http://kingarthurmovie.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT02H06M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "King Arthur: Legend of the Sword 3D (2017)",
            "lang": "en"
        },
        "uri": "assets/p12394972_p_v5_ae.jpg",
        "category": "Poster Art",
        "text": "yes"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:20",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:20",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:20",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:20",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T13:25",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T19:10",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T22:15",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T12:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T18:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T21:30",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T13:10",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T19:20",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T22:25",
        "barg": false
    }]
}, {
    "tmsId": "MV009961350000",
    "rootId": "12343481",
    "subType": "Feature Film",
    "title": "Alien: Covenant -- The IMAX 2D Experience",
    "releaseYear": 2017,
    "releaseDate": "2017-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Science fiction", "Horror", "Thriller"],
    "longDescription": "Bound for a remote planet on the far side of the galaxy, members (Katherine Waterston, Billy Crudup) of the colony ship Covenant discover what they think to be an uncharted paradise. While there, they meet David (Michael Fassbender), the synthetic survivor of the doomed Prometheus expedition. The mysterious world soon turns dark and dangerous when a hostile alien life-form forces the crew into a deadly fight for survival.",
    "shortDescription": "Crew members of a colony ship encounter a hostile alien life-form on a dark and dangerous planet.",
    "topCast": ["Michael Fassbender", "Katherine Waterston", "Billy Crudup"],
    "directors": ["Ridley Scott"],
    "officialUrl": "http://www.foxmovies.com/movies/alien-covenant",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Graphic Violence", "Nudity"],
    "runTime": "PT02H02M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Alien: Covenant (2017)",
            "lang": "en"
        },
        "uri": "assets/p12343481_p_v5_aq.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T13:50",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:45",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:45",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:40",
        "quals": "No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV009821030000",
    "rootId": "13836433",
    "subType": "Feature Film",
    "title": "Bon Cop Bad Cop 2",
    "releaseYear": 2017,
    "releaseDate": "2017",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Action", "Comedy", "Crime drama"],
    "longDescription": "Martin and David meet when they were forced to work together on a crime. Years later, they reunite after they discover a car theft ring that turns out to be a lot more than they bargained for.",
    "shortDescription": "Martin and David reunite when a simple case becomes dangerous.",
    "topCast": ["Colm Feore", "Erik Knudsen", "Sarah-Jeanne Labrosse"],
    "directors": ["Alain Desrochers"],
    "runTime": "PT01H30M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Bon Cop Bad Cop 2 (2017)",
            "lang": "en"
        },
        "uri": "assets/p13836433_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T14:00",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T16:50",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T19:50",
        "barg": false
    }, {
        "theatre": {
            "id": "5683",
            "name": "Scotiabank Theatre Toronto"
        },
        "dateTime": "2017-05-27T22:45",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T21:00",
        "barg": false
    }]
}, {
    "tmsId": "MV009900360000",
    "rootId": "13302334",
    "subType": "Feature Film",
    "title": "Chuck",
    "releaseYear": 2016,
    "releaseDate": "2016-09-02",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Biography", "Historical drama"],
    "longDescription": "He was the pride of Bayonne, N.J., a man who went 15 rounds in the ring with Muhammad Ali. But before all of that, Chuck Wepner was a liquor salesman and father with a modest prizefighting career whose life changed overnight when, in 1975, he was chosen to take on Ali in a highly publicized title match. It's the beginning of a wild ride through the exhilarating highs and humbling lows of sudden fame, but what happens when your 15 minutes in the spotlight are up?",
    "shortDescription": "Embattled New Jersey boxer Chuck Wepner takes on Muhammad Ali.",
    "topCast": ["Liev Schreiber", "Elisabeth Moss", "Naomi Watts"],
    "directors": ["Philippe Falardeau"],
    "officialUrl": "http://www.ifcfilms.com/films/chuck",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Nudity", "Violence"],
    "runTime": "PT01H41M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Chuck (2016)",
            "lang": "en"
        },
        "uri": "assets/p13302334_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T11:10",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:40",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T16:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:10",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:05",
        "barg": false
    }]
}, {
    "tmsId": "MV010082030000",
    "rootId": "14179514",
    "subType": "Feature Film",
    "title": "Sachin: A Billion Dreams",
    "releaseYear": 2017,
    "releaseDate": "2017",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Biography", "Drama"],
    "shortDescription": "The life of Indian cricketer Sachin Tendulkar.",
    "longDescription": "The life of Indian cricketer Sachin Tendulkar.",
    "directors": ["James Erskine"],
    "runTime": "PT02H19M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:00",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:15",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:30",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:40",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }]
}, {
    "tmsId": "MV010053930000",
    "rootId": "14136892",
    "subType": "Feature Film",
    "title": "Half Girlfriend",
    "releaseYear": 2017,
    "releaseDate": "2017-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Romance", "Drama"],
    "shortDescription": "Riya suggests a compromise to Madhav when she agrees to be his \"half girlfriend.\"",
    "longDescription": "Riya suggests a compromise to Madhav when she agrees to be his \"half girlfriend.\"",
    "topCast": ["Arjun Kapoor", "Shraddha Kapoor", "Vikrant Massey"],
    "directors": ["Mohit Suri"],
    "runTime": "PT02H16M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:10",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:20",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:30",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:40",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }]
}, {
    "tmsId": "MV010054010000",
    "rootId": "14137362",
    "subType": "Feature Film",
    "title": "Hindi Medium",
    "releaseYear": 2017,
    "releaseDate": "2017-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy drama"],
    "shortDescription": "A couple want to give their daughter the best education so she will be accepted by the elite.",
    "longDescription": "A couple want to give their daughter the best education so she will be accepted by the elite.",
    "topCast": ["Irrfan Khan", "Saba Qamar", "Deepak Dobriyal"],
    "directors": ["Saket Chaudhary"],
    "runTime": "PT02H13M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:20",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:40",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:50",
        "quals": "Hindi w/e.s.t.",
        "barg": false
    }]
}, {
    "tmsId": "EV000007454359",
    "rootId": "13777665",
    "subType": "Theatre Event",
    "title": "NT Live: Rosencrantz & Guildenstern Are Dead",
    "titleLang": "en",
    "entityType": "Movie",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:50",
        "barg": false
    }, {
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T12:30",
        "barg": false
    }]
}, {
    "tmsId": "MV010007920000",
    "rootId": "14076468",
    "subType": "Feature Film",
    "title": "Battle of Memories",
    "releaseYear": 2017,
    "releaseDate": "2017-04-28",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Mystery", "Thriller"],
    "longDescription": "In 2025, a memory manipulation operation allows people to delete memories. When a man tries to retrieve memories of his failed marriage, he finds himself in a serial killer's mind.",
    "shortDescription": "A man finds himself in a serial killer's mind when he tries to retrieve deleted memories.",
    "topCast": ["Bo Huang", "Yihong Duan", "Eoin O'Brien"],
    "directors": ["Leste Chen"],
    "advisories": ["Adult Situations", "Graphic Violence"],
    "runTime": "PT02H00M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T12:50",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:45",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:40",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:25",
        "barg": false
    }]
}, {
    "tmsId": "MV009141240000",
    "rootId": "13107896",
    "subType": "Feature Film",
    "title": "The Boss Baby",
    "releaseYear": 2017,
    "releaseDate": "2017-03-31",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Adventure", "Animated", "Children"],
    "audience": "Children",
    "longDescription": "A new baby's arrival impacts a family, told from the point of view of a delightfully unreliable narrator -- a wildly imaginative 7-year-old named Tim. The most unusual Boss Baby (Alec Baldwin) arrives at Tim's home in a taxi, wearing a suit and carrying a briefcase. The instant sibling rivalry must soon be put aside when Tim discovers that Boss Baby is actually a spy on a secret mission, and only he can help thwart a dastardly plot that involves an epic battle between puppies and babies.",
    "shortDescription": "A wildly imaginative boy discovers that his new brother is actually a spy on a secret mission.",
    "topCast": ["Alec Baldwin", "Miles Christopher Bakshi", "Tobey Maguire"],
    "directors": ["Tom McGrath"],
    "officialUrl": "http://www.foxmovies.com/movies/the-boss-baby",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H37M",
    "animation": "Animated",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13107896_v_v5_ac.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T15:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T13:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T16:15",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T12:00",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T14:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8311",
            "name": "Alliance Cinemas Beach Cinemas"
        },
        "dateTime": "2017-05-27T17:00",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T16:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009044980000",
    "rootId": "13016067",
    "subType": "Feature Film",
    "title": "What a Wonderful Family!",
    "releaseYear": 2016,
    "releaseDate": "2016-03-12",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy"],
    "longDescription": "The patriarch of a family is enjoying his retirement until his wife of 50 years announces she wants a divorce. Panic stricken, the couple's three adult children are forced to deal with their own relationship problems.",
    "shortDescription": "The patriarch of a family is enjoying his retirement until his wife announces she wants a divorce.",
    "topCast": ["Isao Hashizume", "Kazuko Yoshiyuki", "Masahiko Nishimura"],
    "directors": ["Yôji Yamada"],
    "runTime": "PT01H48M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T16:10",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:50",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T21:40",
        "barg": false
    }]
}, {
    "tmsId": "MV010023360000",
    "rootId": "12009531",
    "subType": "Feature Film",
    "title": "Pirates of the Caribbean: Dead Men Tell No Tales -- The IMAX 2D Experience",
    "releaseYear": 2017,
    "releaseDate": "2017-05-26",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Action", "Fantasy"],
    "longDescription": "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy.",
    "shortDescription": "Deadly ghost sailors pursue Jack Sparrow as he searches for the legendary Trident of Poseidon.",
    "topCast": ["Johnny Depp", "Geoffrey Rush", "Javier Bardem"],
    "directors": ["Joachim Rønning", "Espen Sandberg"],
    "officialUrl": "http://pirates.disney.com/pirates-of-the-caribbean-dead-men-tell-no-tales",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT02H09M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Pirates of the Caribbean: Dead Men Tell No Tales -- The IMAX 2D Experience (2017)",
            "lang": "en"
        },
        "uri": "assets/p12009531_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:20",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T16:25",
        "quals": "No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV010071690000",
    "rootId": "14163838",
    "subType": "Feature Film",
    "title": "29 Plus 1",
    "releaseYear": 2017,
    "releaseDate": "2017",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy drama", "Fantasy"],
    "shortDescription": "Two women form a deep and invisible bond.",
    "longDescription": "Two women form a deep and invisible bond.",
    "topCast": ["Chrissie Chau", "Joyce Cheng", "Elaine Jin"],
    "directors": ["Kearen Pang"],
    "runTime": "PT01H40M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T13:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T16:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:15",
        "barg": false
    }]
}, {
    "tmsId": "MV009246340000",
    "rootId": "13207488",
    "subType": "Feature Film",
    "title": "Your Name",
    "releaseYear": 2016,
    "releaseDate": "2016-08-26",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Anime", "Romance", "Fantasy"],
    "longDescription": "A teenage boy and girl embark on a quest to meet each other for the first time after they magically swap bodies.",
    "shortDescription": "A teenage boy and girl look to meet each other for the first time after they magically swap bodies.",
    "topCast": ["Ryûnosuke Kamiki", "Mone Kamishiraishi", "Etsuko Ichihara"],
    "directors": ["Makoto Shinkai"],
    "officialUrl": "https://www.funimationfilms.com/movie/yourname/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H46M",
    "animation": "Anime",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T16:00",
        "quals": "Japanese w/e.s.t.",
        "barg": false
    }]
}, {
    "tmsId": "MV009141250000",
    "rootId": "13107896",
    "subType": "Feature Film",
    "title": "The Boss Baby 3D",
    "releaseYear": 2017,
    "releaseDate": "2017-03-31",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Adventure", "Animated", "Children"],
    "audience": "Children",
    "longDescription": "A new baby's arrival impacts a family, told from the point of view of a delightfully unreliable narrator -- a wildly imaginative 7-year-old named Tim. The most unusual Boss Baby (Alec Baldwin) arrives at Tim's home in a taxi, wearing a suit and carrying a briefcase. The instant sibling rivalry must soon be put aside when Tim discovers that Boss Baby is actually a spy on a secret mission, and only he can help thwart a dastardly plot that involves an epic battle between puppies and babies.",
    "shortDescription": "A wildly imaginative boy discovers that his new brother is actually a spy on a secret mission.",
    "topCast": ["Alec Baldwin", "Miles Christopher Bakshi", "Tobey Maguire"],
    "directors": ["Tom McGrath"],
    "officialUrl": "http://www.foxmovies.com/movies/the-boss-baby",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H37M",
    "animation": "Animated",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Boss Baby 3D (2017)",
            "lang": "en"
        },
        "uri": "assets/p13107896_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T18:00",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:40",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T11:15",
        "quals": "CC/DVS",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T13:40",
        "quals": "CC/DVS",
        "barg": false
    }]
}, {
    "tmsId": "MV009390740000",
    "rootId": "12009531",
    "subType": "Feature Film",
    "title": "Pirates of the Caribbean: Dead Men Tell No Tales -- An IMAX 3D Experience",
    "releaseYear": 2017,
    "releaseDate": "2017-05-26",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Adventure", "Action", "Fantasy"],
    "longDescription": "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy.",
    "shortDescription": "Deadly ghost sailors pursue Jack Sparrow as he searches for the legendary Trident of Poseidon.",
    "topCast": ["Johnny Depp", "Geoffrey Rush", "Javier Bardem"],
    "directors": ["Joachim Rønning", "Espen Sandberg"],
    "officialUrl": "http://pirates.disney.com/pirates-of-the-caribbean-dead-men-tell-no-tales",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations", "Violence"],
    "runTime": "PT02H09M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Pirates of the Caribbean: Dead Men Tell No Tales -- The IMAX 2D Experience (2017)",
            "lang": "en"
        },
        "uri": "assets/p12009531_p_v5_ad.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T19:30",
        "quals": "No Passes",
        "barg": false
    }, {
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T22:35",
        "quals": "No Passes",
        "barg": false
    }]
}, {
    "tmsId": "MV009405300000",
    "rootId": "13377996",
    "subType": "Feature Film",
    "title": "The Circle",
    "releaseYear": 2017,
    "releaseDate": "2017-04-26",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Thriller", "Drama"],
    "longDescription": "Mae Holland (Emma Watson) seizes the opportunity of a lifetime when she lands a job with the world's most powerful technology and social media company. Encouraged by the company's founder (Tom Hanks), Mae joins a groundbreaking experiment that pushes the boundaries of privacy, ethics and personal freedom. Her participation in the experiment, and every decision she makes soon starts to affect the lives and futures of her friends, family and that of humanity.",
    "shortDescription": "A woman joins an experiment that pushes the boundaries of privacy, ethics and personal freedom.",
    "topCast": ["Emma Watson", "Tom Hanks", "John Boyega"],
    "directors": ["James Ponsoldt"],
    "officialUrl": "http://www.wearethecircle.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H50M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Circle (2017)",
            "lang": "en"
        },
        "uri": "assets/p13377996_p_v5_ab.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10619",
            "name": "Cineplex Cinemas Yonge-Dundas and VIP"
        },
        "dateTime": "2017-05-27T20:30",
        "barg": false
    }]
}, {
    "tmsId": "MV008655890000",
    "rootId": "12671735",
    "subType": "Feature Film",
    "title": "Certain Women",
    "releaseYear": 2016,
    "releaseDate": "2016-01-24",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Drama"],
    "longDescription": "Three strong-willed women (Kristen Stewart, Laura Dern, Michelle Williams) strive to forge their own paths amidst the wide-open plains of the American Northwest: a lawyer who finds herself contending with both office sexism and a hostage situation; a wife and mother whose determination to build her dream home puts her at odds with the men in her life; and a young law student who forms an ambiguous bond with a lonely ranch hand.",
    "shortDescription": "The lives of three women intersect in a small town.",
    "topCast": ["Kristen Stewart", "Laura Dern", "Michelle Williams"],
    "directors": ["Kelly Reichardt"],
    "officialUrl": "http://www.ifcfilms.com/films/certain-women",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H47M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12671735_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T11:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T14:10",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T16:20",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T21:30",
        "barg": false
    }]
}, {
    "tmsId": "MV005474500000",
    "rootId": "10518369",
    "subType": "Feature Film",
    "title": "Risk",
    "releaseYear": 2016,
    "releaseDate": "2016-05-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "Filmmaker Laura Poitras gains unprecedented access to WikiLeaks founder Julian Assange and his team for six years.",
    "shortDescription": "Laura Poitras gains unprecedented access to WikiLeaks founder Julian Assange for six years.",
    "topCast": ["Julian Assange"],
    "directors": ["Laura Poitras"],
    "officialUrl": "http://riskfilm.org/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT01H24M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Risk (2016)",
            "lang": "en"
        },
        "uri": "assets/p10518369_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T11:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T17:00",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T19:30",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T21:40",
        "barg": false
    }]
}, {
    "tmsId": "MV008316860000",
    "rootId": "12384002",
    "subType": "Feature Film",
    "title": "The Commune",
    "releaseYear": 2016,
    "releaseDate": "2016-04-29",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Drama"],
    "longDescription": "You choose your family.",
    "shortDescription": "Personal desires clash with solidarity and tolerance in a Danish commune.",
    "topCast": ["Trine Dyrholm", "Ulrich Thomsen", "Helene Reingaard Neumann"],
    "directors": ["Thomas Vinterberg"],
    "officialUrl": "http://www.communefilm.com/",
    "advisories": ["Adult Situations", "Nudity"],
    "runTime": "PT01H52M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12384002_v_v5_ad.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T13:50",
        "barg": false
    }, {
        "theatre": {
            "id": "10304",
            "name": "TIFF Bell Lightbox"
        },
        "dateTime": "2017-05-27T18:50",
        "barg": false
    }]
}, {
    "tmsId": "MV000008590000",
    "rootId": "546",
    "subType": "Feature Film",
    "title": "Soylent Green",
    "releaseYear": 1973,
    "releaseDate": "1973-04-19",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Science fiction", "Mystery"],
    "longDescription": "In a densely overpopulated, starving New York City of the future, NYPD detective Robert Thorn (Charlton Heston) investigates the murder of an executive at rations manufacturer Soylent Corporation. With the help of elderly academic Solomon \"Sol\" Roth (Edward G. Robinson), Thorn begins to make real progress -- until the governor mysteriously pulls the plug. Obsessed with the mystery, Thorn steps out from behind the badge and launches his own investigation into the murder.",
    "shortDescription": "Futuristic detectives (Charlton Heston, Edward G. Robinson) find a food has a secret ingredient.",
    "topCast": ["Charlton Heston", "Edward G. Robinson", "Leigh Taylor-Young"],
    "directors": ["Richard Fleischer"],
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Brief Nudity", "Violence"],
    "runTime": "PT01H37M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p546_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "48",
            "name": "Camera"
        },
        "dateTime": "2017-05-27T15:00",
        "barg": false
    }]
}, {
    "tmsId": "MV000176130000",
    "rootId": "8299",
    "subType": "Feature Film",
    "title": "The Neverending Story",
    "releaseYear": 1984,
    "releaseDate": "1984-07-20",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Fantasy", "Adventure", "Children"],
    "audience": "Children",
    "longDescription": "On his way to school, Bastian (Barret Oliver) ducks into a bookstore to avoid bullies. Sneaking away with a book called \"The Neverending Story,\" Bastian begins reading it in the school attic. The novel is about Fantasia, a fantasy land threatened by \"The Nothing,\" a darkness that destroys everything it touches. The kingdom needs the help of a human child to survive. When Bastian reads a description of himself in the book, he begins to wonder if Fantasia is real and needs him to survive.",
    "shortDescription": "An imaginative boy is transported to a magical kingdom in danger of destruction.",
    "topCast": ["Barret Oliver", "Noah Hathaway", "Tami Stronach"],
    "directors": ["Wolfgang Petersen"],
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations", "Mild Violence"],
    "runTime": "PT01H32M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p8299_v_v5_ab.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5345",
            "name": "The Revue Cinema"
        },
        "dateTime": "2017-05-27T13:30",
        "barg": false
    }]
}, {
    "tmsId": "MV009445680000",
    "rootId": "13426608",
    "subType": "Feature Film",
    "title": "A Quiet Passion",
    "releaseYear": 2016,
    "releaseDate": "2016-02-13",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Biography", "Historical drama"],
    "longDescription": "Emily Dickinson (Cynthia Nixon) maintains close ties with her family while becoming a prolific poet whose work becomes recognized after her death in 1886.",
    "shortDescription": "Emily Dickinson maintains close ties with her family while becoming a prolific 19th-century poet.",
    "topCast": ["Cynthia Nixon", "Jennifer Ehle", "Keith Carradine"],
    "directors": ["Terence Davies"],
    "officialUrl": "http://www.musicboxfilms.com/a-quiet-passion-movies-153.php",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT02H05M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "A Quiet Passion (2016)",
            "lang": "en"
        },
        "uri": "assets/p13426608_p_v5_ab.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "2524",
            "name": "Regent Theatre"
        },
        "dateTime": "2017-05-27T16:00",
        "barg": false
    }, {
        "theatre": {
            "id": "2524",
            "name": "Regent Theatre"
        },
        "dateTime": "2017-05-27T20:15",
        "barg": false
    }]
}, {
    "tmsId": "MV008227890000",
    "rootId": "12313311",
    "subType": "Feature Film",
    "title": "Going in Style",
    "releaseYear": 2017,
    "releaseDate": "2017-04-07",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy"],
    "longDescription": "Lifelong buddies Willie (Morgan Freeman), Joe (Michael Caine) and Albert (Alan Arkin) decide to buck retirement and step off the straight-and-narrow when their pension funds become a corporate casualty. Desperate to pay the bills and come through for their loved ones, the three men risk it all by embarking on a daring adventure to knock off the very bank that absconded with their money.",
    "shortDescription": "Three lifelong buddies hatch a scheme to rob the bank that took away their pension funds.",
    "topCast": ["Morgan Freeman", "Michael Caine", "Alan Arkin"],
    "directors": ["Zach Braff"],
    "officialUrl": "http://goinginstylemovie.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations", "Violence"],
    "runTime": "PT01H36M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Going in Style (2017)",
            "lang": "en"
        },
        "uri": "assets/p12313311_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "2524",
            "name": "Regent Theatre"
        },
        "dateTime": "2017-05-27T18:15",
        "barg": false
    }]
}, {
    "tmsId": "MV009714510000",
    "rootId": "13689689",
    "subType": "Feature Film",
    "title": "Norman: The Moderate Rise and Tragic Fall of a New York Fixer",
    "releaseYear": 2016,
    "releaseDate": "2016-09-03",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy drama"],
    "longDescription": "Norman (Richard Gere), a New York fixer, knows the right people and can get things done. When an Israeli dignitary named Eshel (Lior Ashkenazi) comes to the city, Norman decides to impress the man by buying him some very expensive shoes. It works and he establishes a strong connection to the man, but a few years later, when Eshel becomes the Israel prime minister, Norman can't communicate with him anymore, and this threatens to destroy his reputation.",
    "shortDescription": "A financial schemer (Richard Gere) finds himself in the middle of an international scandal.",
    "topCast": ["Richard Gere", "Lior Ashkenazi", "Michael Sheen"],
    "directors": ["Joseph Cedar"],
    "officialUrl": "http://sonyclassics.com/norman/#",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "R"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H58M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Norman: The Moderate Rise and Tragic Fall of a New York Fixer (2016)",
            "lang": "en"
        },
        "uri": "assets/p13689689_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T13:00",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T15:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:20",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T21:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV010080670000",
    "rootId": "14178366",
    "subType": "Feature Film",
    "title": "Dear Other Self",
    "releaseYear": 2017,
    "releaseDate": "2017-05-17",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy"],
    "shortDescription": "A woman debates whether to stay with her current job or to pursue her passion for traveling.",
    "longDescription": "A woman debates whether to stay with her current job or to pursue her passion for traveling.",
    "topCast": ["Jodi Sta. Maria", "Xian Lim", "Joseph Marco"],
    "directors": ["Verónica Velasco"],
    "runTime": "PT01H50M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T13:20",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T16:05",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:30",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T21:20",
        "barg": false
    }]
}, {
    "tmsId": "MV007877580000",
    "rootId": "11993778",
    "subType": "Feature Film",
    "title": "Smurfs: The Lost Village",
    "releaseYear": 2017,
    "releaseDate": "2017-04-07",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Adventure", "Fantasy", "Animated", "Children"],
    "audience": "Children",
    "longDescription": "Best friends Smurfette (Demi Lovato), Brainy (Danny Pudi), Clumsy (Jack McBrayer) and Hefty (Joe Manganiello) use a special map that guides them through the Forbidden Forest, an enchanted wonderland that's filled with magical creatures. Their adventure leads them on a course to discover the biggest secret in Smurf history as they race against time and the evil wizard Gargamel (Rainn Wilson) to find a mysterious village.",
    "shortDescription": "The Smurfs embark on a journey through the Forbidden Forest to find a mysterious village.",
    "topCast": ["Demi Lovato", "Rainn Wilson", "Joe Manganiello"],
    "directors": ["Kelly Asbury"],
    "officialUrl": "http://www.smurfsmovie.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H31M",
    "animation": "Animated",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p11993778_v_v5_ad.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T13:30",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T15:45",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:50",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV008738450000",
    "rootId": "12737739",
    "subType": "Feature Film",
    "title": "Born in China",
    "releaseYear": 2016,
    "releaseDate": "2016-08-05",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "From frigid mountains to the heart of the bamboo forest, filmmaker Lu Chuan follows the adventures of three animal families in China: the majestic panda, the savvy golden monkey and the elusive snow leopard.",
    "shortDescription": "The adventures of three animal families in China: majestic pandas, golden monkeys and snow leopards.",
    "topCast": ["John Krasinski"],
    "directors": ["Lu Chuan"],
    "officialUrl": "http://nature.disney.com/born-in-china",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "G"
    }],
    "runTime": "PT01H19M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "Born in China (2016)",
            "lang": "en"
        },
        "uri": "assets/p12737739_p_v5_ab.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T13:40",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009074370000",
    "rootId": "13045694",
    "subType": "Feature Film",
    "title": "Gifted",
    "releaseYear": 2017,
    "releaseDate": "2017-04-07",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Drama"],
    "longDescription": "Frank Adler (Chris Evans) is a single man raising a child prodigy - his spirited young niece Mary (Mckenna Grace) - in a coastal town in Florida. Frank's plans for a normal school life for Mary are foiled when the 7-year-old's mathematical abilities come to the attention of Frank's formidable mother, Evelyn (Lindsay Duncan), whose plans for her granddaughter threaten to separate Frank and Mary.",
    "shortDescription": "A man (Chris Evans) wages a legal battle against his mother for custody of his brilliant niece.",
    "topCast": ["Chris Evans", "Mckenna Grace", "Lindsay Duncan"],
    "directors": ["Marc Webb"],
    "officialUrl": "http://www.foxsearchlight.com/gifted/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Language", "Adult Situations"],
    "runTime": "PT01H41M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13045694_v_v5_aa.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T16:10",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T18:35",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }, {
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T21:25",
        "quals": "Closed Caption & Descriptive Video",
        "barg": false
    }]
}, {
    "tmsId": "MV009039380000",
    "rootId": "13010059",
    "subType": "Feature Film",
    "title": "The Zookeeper's Wife",
    "releaseYear": 2017,
    "releaseDate": "2017-03-31",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Biography", "Historical drama"],
    "longDescription": "The time is 1939 and the place is Poland, homeland of Antonina Zabinski and her husband, Dr. Jan Zabinski. The Warsaw Zoo flourishes under Jan's stewardship and Antonina's care. When their country is invaded by the Nazis, Jan and Antonina are forced to report to the Reich's newly appointed chief zoologist, Lutz Heck. The Zabinskis covertly begin working with the Resistance and put into action plans to save the lives of hundreds from what has become the Warsaw Ghetto.",
    "shortDescription": "Keepers of the Warsaw Zoo help save hundreds of people from Nazi hands during World War II.",
    "topCast": ["Jessica Chastain", "Johan Heldenbergh", "Michael McElhatton"],
    "directors": ["Niki Caro"],
    "officialUrl": "http://www.focusfeatures.com/thezookeeperswife",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG-13"
    }],
    "advisories": ["Adult Situations", "Nudity", "Violence"],
    "runTime": "PT02H05M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "caption": {
            "content": "The Zookeeper's Wife (2017)",
            "lang": "en"
        },
        "uri": "assets/p13010059_p_v5_aa.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8798",
            "name": "Famous Players Canada Square Cinemas"
        },
        "dateTime": "2017-05-27T21:05",
        "barg": false
    }]
}, {
    "tmsId": "MV008375490000",
    "rootId": "12443929",
    "subType": "Feature Film",
    "title": "Storks",
    "releaseYear": 2016,
    "releaseDate": "2016-09-23",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Comedy", "Adventure", "Animated", "Children"],
    "audience": "Children",
    "longDescription": "Storks deliver babies -- or at least they used to. Now, they deliver packages for a global internet retail giant. Junior (Andy Samberg), the company's top delivery stork, lands in hot water when the Baby Factory produces an adorable but wholly unauthorized girl. Desperate to deliver this bundle of trouble, Junior and his friend Tulip (Katie Crown), the only human on Stork Mountain, race against time to make their first baby drop before the boss (Kelsey Grammer) finds out.",
    "shortDescription": "A stork (Andy Samberg) and his human friend race against time to make their first baby drop.",
    "topCast": ["Andy Samberg", "Katie Crown", "Kelsey Grammer"],
    "directors": ["Nicholas Stoller", "Doug Sweetland"],
    "officialUrl": "http://www.storksmovie.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "2.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H29M",
    "animation": "Animated",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12443929_v_v5_ac.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "5675",
            "name": "Cineplex Cinemas Yonge-Eglinton and VIP"
        },
        "dateTime": "2017-05-27T11:00",
        "barg": false
    }, {
        "theatre": {
            "id": "7582",
            "name": "SilverCity Yorkdale Cinemas"
        },
        "dateTime": "2017-05-27T11:00",
        "barg": false
    }]
}, {
    "tmsId": "MV009643870000",
    "rootId": "13595194",
    "subType": "Feature Film",
    "title": "The Wedding Plan",
    "releaseYear": 2016,
    "releaseDate": "2016-08-31",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Romantic comedy"],
    "longDescription": "After her fiance calls off their wedding a month before the ceremony, a woman decides to keep the reservation and trusts God will provide her with a husband.",
    "shortDescription": "After a breakup, a woman keeps her wedding reservation and hopes God will provide a husband.",
    "topCast": ["Noa Koler", "Amos Tamam", "Oz Zehavi"],
    "directors": ["Rama Burshtein"],
    "officialUrl": "http://www.theweddingplanmovie.com/",
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "PG"
    }],
    "advisories": ["Adult Situations"],
    "runTime": "PT01H50M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p13595194_v_v5_ab.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "2523",
            "name": "Mt. Pleasant Theatre"
        },
        "dateTime": "2017-05-27T15:40",
        "barg": false
    }, {
        "theatre": {
            "id": "2523",
            "name": "Mt. Pleasant Theatre"
        },
        "dateTime": "2017-05-27T18:15",
        "barg": false
    }, {
        "theatre": {
            "id": "2523",
            "name": "Mt. Pleasant Theatre"
        },
        "dateTime": "2017-05-27T20:45",
        "barg": false
    }]
}, {
    "tmsId": "MV009689040000",
    "rootId": "13656799",
    "subType": "Short Film",
    "title": "Dream Big: Engineering Our World",
    "releaseYear": 2017,
    "releaseDate": "2017-02-17",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "Filmmaker Greg MacGillivray explores the human ingenuity behind engineering marvels -- big and small -- and reveals the heart that drives engineers to create better lives for people around the world.",
    "shortDescription": "A celebration of the human ingenuity behind engineering marvels.",
    "topCast": ["Jeff Bridges"],
    "directors": ["Greg MacGillivray"],
    "runTime": "PT00H40M",
    "preferredImage": {
        "uri": "tvbanners/generic/generic_tvbanners_v5.png"
    },
    "showtimes": [{
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T11:00",
        "barg": false
    }, {
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T13:00",
        "barg": false
    }, {
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T15:00",
        "barg": false
    }, {
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T17:00",
        "barg": false
    }, {
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T19:00",
        "barg": false
    }]
}, {
    "tmsId": "MV008202030000",
    "rootId": "12286538",
    "subType": "Feature Film",
    "title": "A Beautiful Planet",
    "releaseYear": 2016,
    "releaseDate": "2016-04-29",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "Astronauts aboard the International Space Station capture breathtaking footage of the natural wonders of Earth.",
    "shortDescription": "Astronauts aboard the International Space Station capture breathtaking footage of Earth.",
    "topCast": ["Jennifer Lawrence"],
    "directors": ["Toni Myers"],
    "officialUrl": "http://abeautifulplanet.imax.com/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "G"
    }],
    "runTime": "PT00H45M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p12286538_p_v5_ac.jpg",
        "category": "Poster Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T12:00",
        "barg": false
    }, {
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T18:00",
        "barg": false
    }]
}, {
    "tmsId": "MV003736530000",
    "rootId": "8858582",
    "subType": "Short Film",
    "title": "Rocky Mountain Express",
    "releaseYear": 2011,
    "releaseDate": "2011-09-30",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "A history of the nation's first transcontinental railway accompanies a steam-train ride through the Canadian Rockies.",
    "shortDescription": "A trip through the Canadian Rockies shows a history of the nation's first transcontinental railway.",
    "directors": ["Stephen Low"],
    "runTime": "PT00H40M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p8858582_i_v5_aa.jpg",
        "category": "Iconic",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T14:00",
        "barg": false
    }]
}, {
    "tmsId": "MV002432080000",
    "rootId": "190736",
    "subType": "Short Film",
    "title": "Under the Sea",
    "releaseYear": 2009,
    "releaseDate": "2009-02-13",
    "titleLang": "en",
    "descriptionLang": "en",
    "entityType": "Movie",
    "genres": ["Documentary"],
    "longDescription": "People come face to face with mysterious and stunning creatures of the ocean off Australia and New Guinea.",
    "shortDescription": "Mysterious and stunning creatures of the ocean come into view off Australia and New Guinea.",
    "topCast": ["Jim Carrey"],
    "directors": ["Howard Hall"],
    "officialUrl": "http://www.imax.com/underthesea/",
    "qualityRating": {
        "ratingsBody": "TMS",
        "value": "3.5"
    },
    "ratings": [{
        "body": "Motion Picture Association of America",
        "code": "G"
    }],
    "runTime": "PT00H35M",
    "preferredImage": {
        "width": "240",
        "height": "360",
        "uri": "assets/p190736_v_v5_ab.jpg",
        "category": "VOD Art",
        "text": "yes",
        "primary": "true"
    },
    "showtimes": [{
        "theatre": {
            "id": "8294",
            "name": "Ontario Science Centre OMNIMAX"
        },
        "dateTime": "2017-05-27T16:00",
        "barg": false
    }]
}]
"""
