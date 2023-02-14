import Axios from '@/services/Axios';

export default {
  async login(username, password, token) {
    const payload = { username, password, fcmtoken: token };
    let response = null;

    try {
      response = await Axios.post('/login', payload);
    } catch (e) {
      console.error(e.response.data.message);
      return response;
    }
    response = response.data.data;

    return response;
  },
};
