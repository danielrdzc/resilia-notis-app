import Axios from '@/services/Axios';

export default {
  async getPendingCommissionRequests(userId) {
    const params = { user_id: userId };
    let response = null;

    try {
      response = await Axios.get('/commission_request/pending', { params: params });
    } catch (e) {
      console.error(e.response.data.message);
      return response;
    }
    response = response.data.data;

    return response;
  },
  async getOngoingCommissionRequests(userId) {
    const params = { user_id: userId };
    let response = null;

    try {
      response = await Axios.get('/commission_request/ongoing', { params: params });
    } catch (e) {
      console.error(e.response.data.message);
      //response = new ErrorResponse(e.response.data);
      return response;
    }
    response = response.data.data;

    return response;
  },
  async createCommissionRequests(requestingUserId, artistUserId, requestType) {
    const payload = { requesting_user_id: requestingUserId, artist_user_id: artistUserId,  request_type: requestType, status: 1 };
    let response = null;

    try {
      response = await Axios.post('/commission_request', payload);
    } catch (e) {
      console.error(e.response.data.message);
      //response = new ErrorResponse(e.response.data);
      return response;
    }
    response = response.data;

    return response;
  },
  async updateCommissionRequests(commissionRequestId, status) {
    const payload = { status: status };
    let response = null;

    try {
      response = await Axios.put(`/commission_request/${commissionRequestId}`, payload);
    } catch (e) {
      console.error(e.response.data.message);
      //response = new ErrorResponse(e.response.data);
      return response;
    }
    response = response.data;

    return response;
  },
};
