// custom.js

// Initialize chatbot (example using Dialogflow)
function initChatbot() {
  // Assuming we have a Dialogflow agent setup and we are using Dialogflow's Web Demo integration
  // The iframe embed code from Dialogflow's Web Demo integration would go here
  var iframe = document.createElement('iframe');
  iframe.src = 'https://dialogflow.cloud.google.com/demo?api_key=YOUR_API_KEY';
  iframe.width = '350';
  iframe.height = '430';
  iframe.style.border = 'none';
  document.body.appendChild(iframe);
}
initChatbot();

// Initialize data visualization with D3.js
function initDataVisualization() {
  // Assuming we have a dataset and we want to create a simple bar chart
  var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];
  var svgWidth = 500, svgHeight = 300, barPadding = 5;
  var barWidth = (svgWidth / dataset.length);

  var svg = d3.select('body')
    .append('svg')
    .attr('width', svgWidth)
    .attr('height', svgHeight);

  var barChart = svg.selectAll('rect')
    .data(dataset)
    .enter()
    .append('rect')
    .attr('y', function(d) {
      return svgHeight - d;
    })
    .attr('height', function(d) {
      return d;
    })
    .attr('width', barWidth - barPadding)
    .attr('transform', function (d, i) {
      var translate = [barWidth * i, 0];
      return 'translate(' + translate + ')';
    });
}
initDataVisualization();