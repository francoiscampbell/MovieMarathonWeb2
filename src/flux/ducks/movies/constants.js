function apiUrl(version) {
    return `https://movie-marathon-api.herokuapp.com/${version}/movies/showings`
}

export const API_URL_DEV = apiUrl('mock')
export const API_URL_PROD = apiUrl('v1.1')