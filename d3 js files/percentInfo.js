function aggregate2(json_array, country){
    console.log(country)
    if(country == 'all'){
        var total_confirmed = 0
        var total_recovered = 0
        var total_deaths = 0
        for(i=0; i<json_array.length;i++){
            total_confirmed += parseInt(json_array[i]['confirmed']);
            total_recovered += parseInt(json_array[i]['recovered']);
            total_deaths += parseInt(json_array[i]['deaths']);
        }
        var total_active = total_confirmed - total_recovered - total_deaths;
        return [total_confirmed, total_recovered, total_deaths, total_active];
    }
    else{
        for(i=0; i<json_array.length; i++){
            if(json_array[i]['name'] == country){
                return [json_array[i]['confirmed'], json_array[i]['recovered'], json_array[i]['deaths'], json_array[i]['active']]
            }
        }
    }
}



function worldPercent(country){

    d3.tsv('world_population.tsv', function(data_population){

        console.log(data_population)

        var width = document.getElementById('statusDiv').offsetWidth;
        var height = document.getElementById('statusDiv').offsetHeight;

        d3.selectAll('#statusNode').selectAll('*').remove()

        var svg = d3.selectAll('#statusNode')
                    .append('g')
                    .attr('width', width)
                    .attr('height', height);

        d3.tsv("world_covid.tsv", function(data) {

            var aggregation = aggregate2(data, country);

            if(country == 'all'){
                var percent_of_world_infected = (aggregation[0]/7794798739) * 100;
            }
            else{
                for(i=0; i<data_population.length; i++){
                    if(data_population[i]['name'] == country){
                        var percent_of_world_infected = (aggregation[0]/parseInt(data_population[i]['population'])) * 100;
                    }
                }
            }


            var percent_str = (percent_of_world_infected + '').substr(0,6) + '%'

            svg.selectAll('#statusNode')
                .data(percent_str)
                .enter()
                .append('text')
                .text(percent_str)
                .attr('x', 0.1881*width)
                .attr('y', 60)
                .style('fill', 'white')
                .style('font-size', 0.11*width + 'px')
                .append('svg:tspan')
                // .text(country == 'all' ? '':'People infected in ' + country)
                .text(country == 'all' ? 'Percentage of world infected':'People infected in ')
                
                //.text(country)
                .attr('x', 0.1881*width)
                .attr('y', 90)
                .style('fill', 'white')
                .style('font-size', 0.05*width + 'px')
                .append('svg:tspan')


                .text(country == 'all' ? '': country)
                
                //.text(country)
                .attr('x', 0.1881*width)
                .attr('y', 120)
                .style('fill', 'white')
                .style('font-size', 0.05*width + 'px')
                .append('svg:tspan')

        });
    })

}