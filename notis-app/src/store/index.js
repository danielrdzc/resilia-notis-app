import { createStore } from 'vuex'

export default createStore({
  state() {
    return {
      notiReceivedFlag: false
    }
  },
  getters: {
    notiReceivedFlag: state => state.notiReceivedFlag
  },
  mutations: {
    notiReceived(state) {
      state.notiReceivedFlag = true;
    },
    notiDismissed(state) {
      state.notiReceivedFlag = false;
    },
  },
  actions: {
  },
  modules: {
  }
})
