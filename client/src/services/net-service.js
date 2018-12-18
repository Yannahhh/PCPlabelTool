import axios from 'axios';

const devApiUrl = 'http://localhost:5003/api';

const GET_REQUEST = 'get';
const POST_REQUEST = 'post';

function request(url, params, type, callback) {
    let func;
    if (type === GET_REQUEST) {
        func = axios.get;
    } else if (type === POST_REQUEST) {
        func = axios.post;
    }

    func(url, params).then((response) => {
        if (response.status === 200) {
            callback(response);
        } else {
            console.error(response);
        }
    })
    .catch((error) => {
        console.error(error);
    });
}

function getImages(callback) {
    const url = `${devApiUrl}/images`;
    const params = {};
    request(url, params, GET_REQUEST, callback);
}

function getImage(imageId, callback) {
    const url = `${devApiUrl}/image/${imageId}`;
    const params = {};
    request(url, params, GET_REQUEST, callback);
}

function saveResult(rs, callback) {
    const url = `${devApiUrl}/saveResult`;
    const params = { rs };
    request(url, params, POST_REQUEST, callback);
}


export default {
    getImages,
    getImage,
    saveResult,
};

