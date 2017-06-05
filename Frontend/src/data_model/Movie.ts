export interface Caption {
    content: string;
    lang: string;
}

export interface Movie {
    tmsId: string;
    rootId: string;
    subType: string;
    title: string;
    releaseYear: number;
    releaseDate: string;
    titleLang: string;
    descriptionLang: string;
    entityType: string;
    genres: string[];
    longDescription: string;
    shortDescription: string;
    directors: string[];
    officialUrl: string;
    qualityRating: QualityRating;
    runTime: string;
    preferredImage: PreferredImage;
    showtimes: Showtime[];
    topCast: string[];
    ratings: Rating[];
    advisories: string[];
    audience: string;
    animation: string;
}

export interface PreferredImage {
    width: string;
    height: string;
    uri: string;
    category: string;
    text: string;
    primary: string;
    caption: Caption;
}

export interface QualityRating {
    ratingsBody: string;
    value: string;
}

export interface Rating {
    body: string;
    code: string;
}

export interface Showtime {
    theatre: Theatre;
    dateTime: string;
    barg: boolean;
    quals: string;
}

export interface Theatre {
    id: string;
    name: string;
    movies: Movie[] //added
}
