<template>
    <div>
      <!-- 显示加载动画的部分 -->
      <div v-show="loading" class="loading-overlay">
        <span>Loading...</span>
      </div>
  
      <!-- 显示实际数据的部分 -->
      <div v-show="!loading">
        <!-- 在这里显示后端返回的数据 -->
        {{ responseData }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        loading: true, // 控制加载动画的显示
        responseData: null, // 存储后端返回的数据
      };
    },
    mounted() {
      // 模拟后端数据请求，可以替换成实际的后端请求逻辑
      this.fetchDataFromBackend();
    },
    methods: {
      fetchDataFromBackend() {
        // 模拟后端请求延时
        setTimeout(() => {
          // 假设后端返回的数据是一个字符串 "Hello, World!"
          this.responseData = "Hello, World!";
          this.loading = false; // 数据加载完成，隐藏加载动画
        }, 2000); // 模拟2秒后返回数据
      },
    },
  };
  </script>
  
  <style>
  .loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  