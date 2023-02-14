import Axios from '@/services/Axios';

export default {
  async getAllArtists() {
    let response = null;

    try {
      response = await Axios.get('/user/artists');
    } catch (e) {
      console.error(e.response.data.message);
      return response;
    }
    response = response.data.data;

    return response;
  }
};
