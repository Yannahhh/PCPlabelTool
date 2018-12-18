
let instance = null;
class Service {
    constructor() {
        if (!instance) {
            instance = this;
        }

        this.devApiUrl = 'http://localhost:5003/api';

        return instance;
    }
}

const DataService = new Service();
export default DataService;
