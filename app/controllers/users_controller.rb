class UsersController < ApplicationController
  def index
    User.where("name = '#{params[:name]}'")
  end
end
