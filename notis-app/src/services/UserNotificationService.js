import Axios from '@/services/Axios';

export default {
  async getAllNotis(userId) {
    const params = { user_id: userId };
    let response = null;

    try {
      response = await Axios.get('/user_notification/all', { params: params });
    } catch (e) {
      console.error(e.response.data.message);
      return response;
    }
    response = response.data.data;

    return response;
  }
};
