<!-- Navbar.vue -->
<template>
   
    <div class="navbar" style = "z-index: 0;">
      <div class="content_header" style="clear: both; overflow: hidden;">
        <div class="function_title">
            <img src="../images/icon.png" alt="CleverPDF Word" style="margin-left:0; width: 30px;height: 30px;" />
            <h1 style="margin-left:10px;" id="wtp_title">高光谱图像分析</h1>
            <h2 class="function_title_promit" id="wtp_promit">2023软件工程作业</h2>
        </div>
        </div>
      <div style = "z-index: 2;" class="menu-item" @mouseover="showDescription('用于高光谱分析的网站')" @mouseout="hideDescription">
        项目介绍
        <div v-if="showHoverText" class="hover-text">{{ hoverText }}</div>
      </div>
      <div style = "z-index: 2;"  class="menu-item" @mouseover="showDescription('2023软件工程1组')" @mouseout="hideDescription">
        成员介绍
        <div v-if="showHoverText" class="hover-text">{{ hoverText }}</div>
      </div>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        showHoverText: false,
        hoverText: ''
      };
    },
    methods: {
      showDescription(text) {
        this.showHoverText = true;
        this.hoverText = text;
      },
      hideDescription() {
        this.showHoverText = false;
        this.hoverText = '';
      }
    }
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    background-color: white;
    color: black;
  }
  
  .menu-item {
    padding: 10px;
    cursor: pointer;
    position: relative;
    width: 10%;
  }
  
  .hover-text {
    position: absolute;
    top : 50%;
    left: 0;
    background-color:lightgrey;
    padding: 2px;
    display: none;
  }
  
  .menu-item:hover .hover-text {
    display: block;
  }
  
.function_title_promit {
    width: 100%;
    margin-top: 10px;
    font-size: 16px;
    color: #555;
    line-height: 20px;
    font-weight: 400;
    margin-left: 0;
    margin-right: 0;
    float: left
}

.function_title {
    width: 450px;
    color: #167ebc;
    margin-top: 33px;
    clear: both;
    overflow: hidden;
    float: left;
    padding-left: 10px
}

.function_title h1 {
    float: left;
    color: #0e5d8b;
    line-height: 22px;
    font-size: 22px;
    margin: 0;
    font-weight: 400
}

.function_title img {
    float: left
}

  </style>
  