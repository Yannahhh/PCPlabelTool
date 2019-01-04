<template>
<div>
    <img ref="imageel" id="imagediv" v-bind:src="imageUrl" height="600px">
    <div ref="boundingBoxdiv" id="boundingBox"></div>
    <div class="axisdiv" v-for="onePCP in currentLabels">
        <input placeholder="Enter axisNum" v-model="onePCP.axisNum">
        <button type="button" class="btn" v-on:click="deleteLabel(onePCP.PCPIdx)">Delete</button>
    </div>
        <button type="button" class="btn" v-on:click="prevImage">Prev</button>
        <button type="button" class="btn" v-on:click="nextImage">Next</button>
        <button type="button" class="btn" v-on:click="labelImage">Label</button>
        <button type="button" class="btn" v-on:click="saveResult">Save</button>
    </div>
</div>
</template>

<script>
    import * as d3 from 'd3';
    import NetService from './services/net-service';
    import DataService from './services/data-service';

    export default {
        name: 'App',
        components: {

        },
        data() {
            return {
                imageList: [],
                rs: [],
                currentIdx: 0, // default is 0
                currentLabels: [],
                PCPCount: 0,
                imageUrl: '',
                isMouseDown: false,
                initx: 0,
                inity: 0,
                endx: 0,
                endy: 0,
            };
        },
        mounted() {
            NetService.getImages((resp) => {
                this.imageList = resp.data;
                this.imageUrl = `${DataService.devApiUrl}/image/${this.imageList[0]}`;
            });

            const el = this.$refs.boundingBoxdiv;
            d3.select(el).append('svg')
                .attr('id', 'mainsvg')
                .attr('width', 6000)
                .attr('height', 600)
                .append('g')
                .attr('id', 'svgdrager');

            d3.selectAll('rect').remove();
            d3.select('#mainsvg')
                .on('mousedown', () => {
                    this.initx = d3.mouse(d3.event.currentTarget)[0];
                    this.inity = d3.mouse(d3.event.currentTarget)[1];
                    this.isMouseDown = true;
                    this.PCPCount += 1;
                    d3.select('#svgdrager').append('g')
                        .attr('id', `PCP_${this.PCPCount}`);
                })
                .on('mousemove', () => {
                    if (this.isMouseDown === true) {
                        d3.select(`#PCP_${this.PCPCount}`).selectAll('rect').remove();
                        d3.select(`#PCP_${this.PCPCount}`).append('rect')
                            .attr('x', this.initx)
                            .attr('y', this.inity)
                            .attr('width', d3.mouse(d3.event.currentTarget)[0] - this.initx)
                            .attr('height', d3.mouse(d3.event.currentTarget)[1] - this.inity)
                            .style('fill-opacity', 0.0)
                            .style('stroke', 'red')
                            .style('stroke-width', 2);
                    }
                })
                .on('mouseup', () => {
                    if (this.isMouseDown === true) {
                        this.endx = d3.mouse(d3.event.currentTarget)[0];
                        this.endy = d3.mouse(d3.event.currentTarget)[1];
                        this.currentLabels.push({
                            x: this.initx,
                            y: this.inity,
                            width: this.endx - this.initx,
                            height: this.endy - this.inity,
                            axisNum: 2,
                            PCPIdx: this.PCPCount,
                        });
                    }
                    this.isMouseDown = false;
                });
        },

        methods: {
            prevImage() {
                if (this.currentIdx > 0) {
                    d3.selectAll('rect').remove();
                    this.currentIdx -= 1;
                    this.imageUrl = `${DataService.devApiUrl}/image/${this.imageList[this.currentIdx]}`;
                    this.currentLabels = [];
                    this.PCPCount = 0;
                }
            },

            nextImage() {
                if (this.currentIdx < this.imageList.length - 1) {
                    d3.selectAll('rect').remove();
                    this.currentIdx += 1;
                    this.imageUrl = `${DataService.devApiUrl}/image/${this.imageList[this.currentIdx]}`;
                    this.currentLabels = [];
                    this.PCPCount = 0;
                }
            },

            labelImage() {
                if (this.currentIdx >= this.rs.length) {
                    this.rs.push({
                        imageId: this.imageList[this.currentIdx],
                        imageWidth: d3.select('#imagediv').node().getBoundingClientRect().width,
                        imageHeight: d3.select('#imagediv').node().getBoundingClientRect().height,
                        labels: this.currentLabels,
                    });
                } else {
                    this.rs[this.currentIdx] = {
                        imageId: this.imageList[this.currentIdx],
                        imageWidth: d3.select('#imagediv').node().getBoundingClientRect().width,
                        imageHeight: d3.select('#imagediv').node().getBoundingClientRect().height,
                        labels: this.currentLabels,
                    };
                }
            },

            deleteLabel(PCPIdx) {
                d3.select(`#PCP_${PCPIdx}`).selectAll('rect').remove();
                const arr = this.currentLabels.map(e => e.PCPIdx);
                this.currentLabels.splice(arr.indexOf(PCPIdx), 1);
            },

            saveResult() {
                NetService.saveResult(this.rs, () => {
                });
            },
        },

    };
</script>

<style scoped>
    #imagediv {
        top: 0px;
        left: 0px;
        margin: 0px 0px 0px 0px;
        z-index: 10;
    }

    #boundingBox {
        position: absolute;
        top: 8px;
        left: 0px;
        margin: 0px 0px 0px 0px;
    }

    #boundingBox {
        z-index: 100!important;
    }
</style>

