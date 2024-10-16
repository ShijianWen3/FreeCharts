from pyecharts.charts import *
from pyecharts import options as opts
import numpy

#存放图表类相关的全局方法和属性
class global_opts:
     def __init__(self) -> None:
          self.opt=False

     

class bar_generation(global_opts):
    def __init__(self,title:str,x:list,y:list,dataname:str='') -> None:
         super().__init__()
         #后续希望改成链式调用
         self.bar=Bar()
         self.bar.add_xaxis(x)
         self.bar.add_yaxis(dataname,y)
         self.bar.set_global_opts(
              title_opts=opts.TitleOpts(title=title),
              toolbox_opts=opts.ToolboxOpts(is_show=True,feature=opts.ToolBoxFeatureOpts(save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color='#fff'))),
         )
         #结果路径
         self.result=self.bar.render('./results/result.html')

class line_generation(global_opts):
     def __init__(self,title:str,x:list,y:list,dataname:str='') -> None:
          super().__init__()
          self.line=Line()
          self.line.add_xaxis(x)
          self.line.add_yaxis(
          series_name=dataname,
          y_axis=y,
          symbol="emptyCircle",
          is_symbol_show=True,
          label_opts=opts.LabelOpts(is_show=True),
          is_connect_nones=True
          )

          self.line.set_global_opts(
               title_opts=opts.TitleOpts(title=title),
               toolbox_opts=opts.ToolboxOpts(is_show=True,feature=opts.ToolBoxFeatureOpts(save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color='#fff'))),
          )

          self.result=self.line.render('./results/result.html')


class scatter_generation(global_opts):
     def __init__(self,title:str,x:list,y:list,dataname:str='',is_fitted:bool=False) -> None:
          super().__init__()
          # self.scatter=Scatter()
          self.x_data:list=x
          self.y_data:list=y
          self.x_data = [float(_) for _ in self.x_data]
          self.y_data = [float(_) for _ in self.y_data]
          print(self.x_data)
          print(self.y_data)
          # self.scatter=Scatter().add_xaxis(xaxis_data=self.x_data).add_yaxis(series_name=dataname,y_axis=self.y_data)
          self.scatter=(
          Scatter()
          .add_xaxis(xaxis_data=self.x_data)
          .add_yaxis(
               series_name=dataname,
               y_axis=self.y_data,
               # symbol_size=20,
               # label_opts=opts.LabelOpts(is_show=True),
          )
          .set_series_opts()
          .set_global_opts(
               title_opts=opts.TitleOpts(title=title),
               toolbox_opts=opts.ToolboxOpts(is_show=True,feature=opts.ToolBoxFeatureOpts(save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color='#fff'))),
               xaxis_opts=opts.AxisOpts(
                    type_='value',splitline_opts=opts.SplitLineOpts(is_show=True)
               ),
               yaxis_opts=opts.AxisOpts(
                    type_='value',
                    # axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
               ),
          )
          )
          
          # self.scatter.set_global_opts( 
          #      title_opts=opts.TitleOpts(title=title),
          #      toolbox_opts=opts.ToolboxOpts(is_show=True,feature=opts.ToolBoxFeatureOpts(save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(background_color='#fff'))),
          #      xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
          #      yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
          # )
          if is_fitted:
               self.fit_line()
          else:
               self.result=self.scatter.render('./results/result.html')
     
     def fit_line(self):
          line = Line()
          line.add_xaxis(self.x_data)
          #使用numpy.polyfit拟合直线
          data_x = [float(_) for _ in self.x_data]
          data_y = [float(_) for _ in self.y_data]
          coefficients = numpy.polyfit(data_x, data_y, 1)  # 一次多项式（直线）
          slope, intercept = coefficients
          y_fit = [slope * x + intercept for x in data_x]
          line.add_yaxis(f"拟合直线:Y={slope}X+{intercept}", y_fit, is_smooth=True, linestyle_opts=opts.LineStyleOpts(color="red"),label_opts=opts.LabelOpts(is_show=False))
          # 将散点图和拟合线叠加
          self.scatter.overlap(line)
          self.result=self.scatter.render('./results/result.html')

if __name__=='__main__':
     # scatter_generation('水果数量',['香蕉','苹果','梨子','桃子'],[12,34,56,2],'数量',True)
     pass